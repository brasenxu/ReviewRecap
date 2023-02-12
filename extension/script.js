(() => {
    let isOn = false;
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        let url = tabs[0].url;
        if (url.includes("amazon.") && url.includes("/dp/")) {
            chrome.action.setIcon({ path: "assets/recapOn.png" });
            document.getElementById("section").innerHTML =
                "Click button to recap Amazon reviews.";
            document.getElementById("recapButn").innerHTML =
                '<a href="recap.html" class="btn btn-primary justify-content-center" role="button">RECAP</a>';
            isOn = true;
        } else {
            chrome.action.setIcon({ path: "assets/recapOff.png" });
            document.getElementById("section").innerHTML =
                "Current tab is not able to be recapped.";
            document.getElementById("recapButn").innerHTML =
                '<a class="btn btn-primary justify-content-center disabled" role="button" aria-disabled="true"> RECAP </a>';
            isOn = false;
        }
        const indexdp = url.indexOf("/dp/");

        url = url.substring(19, indexdp + 14);
        const parts = url.split("/");

        if (parts.length == 4) {
            parts.splice(1, 1);
        }

        const newURL = parts.join("/");
        const encodedData = btoa(newURL);

        console.log(encodedData);
    });
})();
