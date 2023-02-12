const checkIcon = () => {

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {

        if (tabs.length === 0 || !tabs[0].url) {
            return;
        }

        if (tabs && tabs[0].url.includes("amazon.") && tabs[0].url.includes("/dp/")) {
            chrome.action.setIcon({ path: "assets/recapOn.png" });
        } else {
            chrome.action.setIcon({ path: "assets/recapOff.png" });
        }

    });

};

chrome.tabs.onUpdated.addListener(checkIcon);
chrome.tabs.onActivated.addListener(checkIcon);
