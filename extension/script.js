const dataFromBackend = {
    "id": "caB09W2JP6SM",
    "data": [
        {
            "keyword": "55",
            "rating": 5.0,
            "freq": 50
        },
        {
            "keyword": "44",
            "rating": 4.0,
            "freq": 40
        },
        {
            "keyword": "33",
            "rating": 3.0,
            "freq": 30
        },
        {
            "keyword": "22",
            "rating": 2.0,
            "freq": 20
        },
        {
            "keyword": "11",
            "rating": 1.0,
            "freq": 10
        }
    ]
};

const data = dataFromBackend.data;
  
const svg = d3.select("svg");
  
const xScale = d3
    .scaleLinear()
    .domain([0, d3.max(dataFromBackend.data, d => d.freq)])
    .range([0, 200]);
  
svg
    .selectAll(".bar")
    .data(dataFromBackend.data)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", 0)
    .attr("y", (d, i) => i * 30)
    .attr("width", d => xScale(d.freq))
    .attr("height", 20);

svg
    .selectAll(".text")
    .data(dataFromBackend.data)
    .enter()
    .append("text")
    .attr("class", "text")
    .attr("x", d => xScale(d.freq) + 5)
    .attr("y", (d, i) => i * 30 + 15)
    .text(d => d.freq);

d3.select("#keyword-column")
    .selectAll("p")
    .data(data)
    .enter()
    .append("p")
    .text(function(d) {
      return d.keyword;
    });


d3.select("#rating-column")
    .selectAll("p")
    .data(data)
    .enter()
    .append("p")
    .text(function(d) {
        return d.rating;
    });


    