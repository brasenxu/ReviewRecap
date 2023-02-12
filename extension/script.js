chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    let url = tabs[0].url;

    if (url.includes("amazon.") && url.includes("/dp/")) {
        chrome.action.setIcon({ path: "assets/recapOn.png" });
        document.getElementById("section").innerHTML =
            "Click button to recap Amazon reviews.";
        document.getElementById("recapButn").innerHTML =
            '<a href="recap.html" class="has-function">RECAP</a>';
    } else {
        chrome.action.setIcon({ path: "assets/recapOff.png" });
        document.getElementById("section").innerHTML =
            "Current tab is not able to be recapped.";
        document.getElementById("recapButn").innerHTML =
            '<a class="no-function">RECAP</a>';
    }
});
