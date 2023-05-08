/* site specific tweaks */
var header = document.querySelector("header");
let previousUrl = "";

// hide header for urls that include 'sandbox'
const observer = new MutationObserver(() => {
  if (location.href !== previousUrl) {
    previousUrl = location.href;
    if (location.href?.includes("sandbox")) {
      header.style.visibility = "hidden";
    } else {
      header.style.visibility = "visible";
    }
  }
});

const config = { subtree: true, childList: true };
observer.observe(document, config);
