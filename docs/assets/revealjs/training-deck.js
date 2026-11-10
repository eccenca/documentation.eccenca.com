/*
 * Runtime for a training deck (the slides.html next to a training page).
 *
 * The deck runs in its own document, inside an <iframe> on the page, so the
 * reveal.js styles never meet the Material theme's. It talks to the page
 * through window.postMessage (assets/training.js is the other side):
 *
 *   deck -> page   { type: "training-deck:ready", slides: [...] }
 *                  { type: "training-deck:slide", id, explainer, title, index, total }
 *   page -> deck   { type: "training-deck:hello" }  (answered with ready + slide)
 *                  { type: "training-deck:goto", id }
 *                  { type: "training-deck:command", command: "next" | "prev" | "notes" }
 *
 * A slide is tied to its explanation on the page by `data-explainer` on the
 * <section>, holding the id of the heading on the page.
 */
(function () {
  "use strict";

  var embedded = window.parent !== window;

  function post(message) {
    if (embedded) {
      window.parent.postMessage(message, window.location.origin === "null" ? "*" : window.location.origin);
    }
  }

  function title(section) {
    var heading = section.querySelector("h1, h2, h3");
    return heading ? heading.textContent.trim() : section.id || "";
  }

  function describe(section) {
    var indices = Reveal.getIndices(section);
    return {
      id: section.id || "",
      explainer: section.getAttribute("data-explainer") || "",
      title: title(section),
      h: indices.h,
      v: indices.v || 0,
    };
  }

  function current() {
    var info = describe(Reveal.getCurrentSlide());
    info.type = "training-deck:slide";
    info.index = Reveal.getSlidePastCount() + 1;
    info.total = Reveal.getTotalSlides();
    return info;
  }

  Reveal.initialize({
    hash: !embedded,
    controls: true,
    controlsTutorial: false,
    progress: true,
    slideNumber: "c/t",
    center: false,
    width: 960,
    height: 540,
    margin: 0.02,
    transition: "slide",
    backgroundTransition: "fade",
    plugins: [RevealMarkdown, RevealNotes],
  }).then(announce);

  function announce() {
    post({ type: "training-deck:ready", slides: Reveal.getSlides().map(describe) });
    post(current());
  }

  Reveal.on("slidechanged", function () {
    post(current());
  });

  window.addEventListener("message", function (event) {
    if (event.source !== window.parent || !event.data || typeof event.data !== "object") {
      return;
    }
    var data = event.data;
    if (data.type === "training-deck:hello") {
      // the page script may start after the deck was ready
      if (Reveal.isReady()) announce();
    } else if (data.type === "training-deck:goto" && data.id) {
      var target = document.getElementById(data.id);
      if (target && target.tagName === "SECTION") {
        var i = Reveal.getIndices(target);
        Reveal.slide(i.h, i.v);
      }
    } else if (data.type === "training-deck:command") {
      if (data.command === "next") Reveal.next();
      if (data.command === "prev") Reveal.prev();
      if (data.command === "notes") {
        var notes = Reveal.getPlugin("notes");
        if (notes) notes.open();
      }
    }
  });
})();
