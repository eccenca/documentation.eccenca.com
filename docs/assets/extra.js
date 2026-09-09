/* site specific tweaks */

// hide header and footer for urls that include 'with-your-sandbox'
var header = document.querySelector("header");
var footer = document.querySelector("footer");
let previousUrl = "";

const observer = new MutationObserver(() => {
  if (location.href !== previousUrl) {
    previousUrl = location.href;
    if (location.href?.includes("with-your-sandbox")) {
      header.style.display = "none";
      footer.style.display = "none";
    } else {
      header.style.display = "block";
      footer.style.display = "block";
    }
  }
});

const config = { subtree: true, childList: true };
observer.observe(document, config);


/* search highlight controls */
//
// Opening a search result loads the page with `?h=<query>`, and the theme wraps
// every match in `<mark data-md-highlight>`. There is no native way to dismiss
// either part, which makes such a URL awkward to hand on, so this block adds a
// button beside the search field that clears both at once.
//
// The parameter is deliberately left alone until the button is used: while the
// page shows highlighting the URL still carries `h`, so a link copied at any
// point reproduces exactly what the sender was looking at. Clicking the button
// takes the marks off the page and `h` off the URL together, so the address bar
// never disagrees with the page.
(function () {
  const MARKS = "mark[data-md-highlight]";
  const LABEL = "Remove search highlighting";

  // material/format-color-marker-cancel.svg inlined: the header draws its icons
  // as inline SVG and this file has no access to the theme's icon loader.
  const ICON =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.5 8C14 8 ' +
    "12 10 12 12.5s2 4.5 4.5 4.5 4.5-2 4.5-4.5S19 8 16.5 8m0 7.5c-1.7 0-3-1.3-3-3 0-.6." +
    "2-1.1.4-1.5l4.1 4.1c-.4.2-.9.4-1.5.4m2.6-1.5L15 9.9c.4-.3.9-.4 1.5-.4 1.7 0 3 1.3 " +
    "3 3 0 .6-.2 1.1-.4 1.5m-7-6.3-1.5-1.5 3.3-3.3c.6-.6 1.5-.6 2.1 0L18.2 5c.4.4.5.8." +
    "4 1.3-.6-.2-1.3-.3-2-.3-1.8 0-3.3.7-4.5 1.7m-1.6 7.2L9 16.3c-.6.6-1.5.6-2.1 0l-.7." +
    '7H2l2.8-2.8c-.6-.6-.6-1.5 0-2.1l4.7-4.7L11.1 9c-.7 1-1.1 2.2-1.1 3.5 0 .8.2 1.6.5 2.4"/></svg>';

  let button = null;
  let seen = "";

  function highlighted() {
    return new URL(location.href).searchParams.has("h");
  }

  function clearHighlight() {
    const parents = new Set();
    document.querySelectorAll(MARKS).forEach((mark) => {
      parents.add(mark.parentNode);
      mark.replaceWith(...mark.childNodes);
    });
    // `replaceWith` leaves the surrounding text split across several nodes;
    // merging them restores the DOM the highlight was applied to.
    parents.forEach((parent) => parent.normalize());

    const url = new URL(location.href);
    url.searchParams.delete("h");
    history.replaceState({}, "", url.toString());

    sync();
  }

  function createButton(search) {
    const element = document.createElement("button");
    element.type = "button";
    element.className = "md-header__button md-icon md-clear-highlight";
    element.title = LABEL;
    element.setAttribute("aria-label", LABEL);
    element.innerHTML = ICON;
    element.addEventListener("click", clearHighlight);
    // Placed before the search field, not after it: the header row is flexible
    // on the title, so a button on this side is absorbed by the title's space
    // and the search field stays put as the button comes and goes.
    search.before(element);
    return element;
  }

  // Offer the button exactly while `h` is in the URL, which is the state the
  // button exists to leave. `navigation.instant` keeps the header across page
  // swaps, so this is re-evaluated per page rather than once at load.
  function sync() {
    const wanted = highlighted();
    if (!button) {
      if (!wanted) return;
      const search = document.querySelector(".md-header .md-search");
      if (!search) return;
      button = createButton(search);
    }
    if (button.hidden === wanted) button.hidden = !wanted;
  }

  // Instant navigation swaps the content without reloading, so the button is
  // re-checked whenever the location changes under it.
  new MutationObserver(() => {
    if (location.href === seen) return;
    seen = location.href;
    sync();
  }).observe(document.body, { subtree: true, childList: true });

  seen = location.href;
  sync();
})();
