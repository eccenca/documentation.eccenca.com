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

