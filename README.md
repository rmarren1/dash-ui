# dash-ui

### Grid
`Grid` makes use of the
[CSS grid](https://css-tricks.com/getting-started-css-grid/)
to make creating dashboard-like layouts super easy in Dash.

##### A Simple Example Grid
This example is found in `simple_demo.py`


First we add the external css url `https://codepen.io/rmarren1/pen/mLqGRg.css`.
This is necessary for the grid to work. If you cannot use this (e.g. you
are serving stylesheets locally) you can just serve the file at https://github.com/rmarren1/dash-ui/blob/master/dash_ui/style/css/grid.css .

Next, we create a grid with the following call:
`grid = dui.Grid(grid_id="grid", num_rows=12, num_cols=12, grid_padding=5)`

* `num_rows` is the number of rows in the grid, and must be between 1 and 12
* `num_cols` is the number of columns in the grid, and must be between 1 and 12
* `grid_padding` is the number of pixels to pad between grid elements, and must
be one of [0, 1, 2, 5, 10, 25, 50, 100].

Now you can add any dash element as a grid element like so:

```
grid.add_element(col=1, row=1, width=3, height=4, element=html.Div(
    style={"background-color": "red", "height": "100%", "width": "100%"}
))
```

* `row` is the starting row in the grid layout
* `col` is the starting column in the grid layout
* `height` is the number of rows the element should span.
* `width` is the number of columns the element should span

Note that the rows and columns are one indexed.

We continue adding elements, then get something like this:


##### An Advanced Grid
This example shows some interactivity into the grid (see `advanced_demo.py`)

We can add plotly graph elements with the shortcut
`grid.add_graph(col=1, row=1, width=3, height=4, graph_id="all-pie")`
which creates a grid element with a graph with the `id` declared in `graph_id`.

We can end up with this really nice interactive dashboard, with only
161 lines of code.
