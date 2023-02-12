function updateRecap({ data }) {

    const svg = d3.select("svg");
    const xScale = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.freq)])
        .range([0, 200]);

    svg.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", 0)
        .attr("y", (d, i) => i * 30)
        .attr("width", (d) => xScale(d.freq))
        .attr("height", 20);

    svg.selectAll(".text")
        .data(data)
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
        .text((d) => d.keyword);

    d3.select("#rating-column")
        .selectAll("p")
        .data(data)
        .enter()
        .append("p")
        .text((d) => d.rating);

}

chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {

    let b64 = ""
    let url = tabs[0].url.split("amazon.")[1].split("/")

    if (url.include("dp")) {
        b64 = btoa(`${url[0]}/${url[2]}/${url[3]}`);
    } else {
        b64 = btoa(`${url[0]}/${url[1]}/${url[2]}`);
    }

    fetch(`http://192.168.96.213:8000/product/${b64}`)
        .then((res) => res.json())
        .then(updateRecap);

});
