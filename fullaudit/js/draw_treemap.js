var format = d3.format(",d");

var color = d3.scaleOrdinal()
        .range(d3.schemeCategory10
          .map(function(c) {
            c = d3.rgb(c);
            c.opacity = 0.6;
            return c;
          }));

var treemap = d3.treemap()
    .size([100, 100])
    .round(true);

d3.json("visualization/output.json", function(error, root) {

  if (error) throw error;

  tree = d3.hierarchy(root)
  treemap(tree
    .sum(function(d) { return d.size; })
    .sort(function(a, b) { return b.height - a.height || b.value - a.value; }));

  d3.select("#graph-container")
    .selectAll(".node")
    .data(tree.leaves())
    .enter().append("div")
      .attr("class", "node")
      .attr("data-toggle", "tooltip")
      .attr("title", function(d) { return d.data.name + "\n" + format(d.value); })
      .style("left", function(d) { return d.x0 + "%"; })
      .style("top", function(d) { return d.y0 + "%"; })
      .style("width", function(d) { return d.x1 - d.x0 + "%"; })
      .style("height", function(d) { return d.y1 - d.y0 + "%"; })
      .style("border", '1px solid white')
      .style("background", function(d) { while (d.depth > 1) d = d.parent; return color(d.data.name); })
    .append("div")
      .attr("class", "node-label")
      .text(function(d) {
        return d.data.name;
      })
    .append("div")
      .attr("class", "node-value")
      .text(function(d) { return format(d.value); });

    d3.select('#graph-legend')
      .selectAll('.legend')
      .data(tree.children)
      .enter().append('div')
        .attr('class', 'legend')
        .style("background", function(d) { return color(d.data.name); })
        .text(function(d) {
          return d.data.name;
        })

    // Bootstrap tooltips have to be activated manually: https://getbootstrap.com/javascript/#tooltips-usage
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })
});

