const getURL = () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        let url = tabs[0].url;
        const indexdp = url.indexOf("/dp/");
        url = url.substring(19, indexdp + 14);
        const parts = url.split("/");

        if (parts.length == 4) {
            parts.splice(1, 1);
        }

        const newURL = parts.join("/");
        const encodedData = btoa(newURL);

        fetch(`http://192.168.96.213:8000/product/${encodedData}`)
            .then((res) => res.json())
            .then((res) => {
                const data = res.data;

                const svg = d3.select("svg");
                const xScale = d3
                    .scaleLinear()
                    .domain([0, d3.max(res.data, (d) => d.freq)])
                    .range([0, 200]);

                svg.selectAll(".bar")
                    .data(res.data)
                    .enter()
                    .append("rect")
                    .attr("class", "bar")
                    .attr("x", 0)
                    .attr("y", (d, i) => i * 30)
                    .attr("width", (d) => xScale(d.freq))
                    .attr("height", 20);

                svg.selectAll(".text")
                    .data(res.data)
                    .enter()
                    .append("text")
                    .attr("class", "text")
                    .attr("x", (d) => xScale(d.freq) + 5)
                    .attr("y", (d, i) => i * 30 + 15)
                    .text((d) => d.freq);

                d3.select("#keyword-column")
                    .selectAll("p")
                    .data(data)
                    .enter()
                    .append("p")
                    .text(function (d) {
                        return d.keyword;
                    });

                d3.select("#rating-column")
                    .selectAll("p")
                    .data(data)
                    .enter()
                    .append("p")
                    .text(function (d) {
                        return d.rating;
                    });
            });
    });
};

getURL();
