import dash_html_components as html
import dash_core_components as dcc


VALID_GRID_PADDINGS = [0, 1, 2, 5, 10, 25, 50, 100]


class Grid:
    def __init__(self, _id="default_grid_id",
                 children=None, num_rows=1, num_cols=1, grid_padding=1):
        if num_rows not in range(1, 13):
            return ValueError(
                "Only 1 to 12 rows supported, not {:d}".format(num_rows))
        if num_cols not in range(1, 13):
            return ValueError(
                "Only 1 to 12 columns supported, not {:d}".format(num_cols))
        if grid_padding not in VALID_GRID_PADDINGS:
            return ValueError(
                "Only grid paddings in "
                + str(VALID_GRID_PADDINGS)
                + "supported")
        self.className = "dui-grid"
        self.children = [] if children is None else children
        self._id = _id
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid_padding = grid_padding

    def add_element(self, element, col, row, width, height, element_class=""):
        if row > self.num_rows:
            raise ValueError(
                "Grid only has {:d} rows, not {:d}".format(
                    self.num_rows, row
                ))
        if row + height - 1 > self.num_rows:
            raise ValueError(
                "Grid only has {:d} rows, not {:d} = {:d} + {:d} - 1".format(
                    self.num_rows, row + height - 1, row, height
                ))
        if col > self.num_cols:
            raise ValueError(
                "Grid only has {:d} columns, not {:d}".format(
                    self.num_cols, col
                ))
        if col + width - 1 > self.num_cols:
            raise ValueError(
                "Grid only has {:d} cols, not {:d} = {:d} + {:d} - 1".format(
                    self.num_cols, col + width - 1, col, width
                ))
        self.children.append(html.Div(
            style={
                "grid-column": "{:d} / span {:d}".format(col, width),
                "grid-row": "{:d} / span {:d}".format(row, height)
            },
            className="dui-grid-element " + element_class,
            children=element
        ))

    def add_graph(self, graph_id, col, row, width, height):
        graph = dcc.Graph(
            id=graph_id,
            style={"width": "100%", "height": "100%"},
            config=dict(
                autosizable=True
            )
        )
        self.add_element(
            element=graph,
            col=col,
            row=row,
            width=width,
            height=height
        )

    def get_component(self):
        grid_class = " ".join([
            self.className,
            "dui-grid-{:d}-rows".format(self.num_rows),
            "dui-grid-{:d}-cols".format(self.num_cols),
            "dui-grid-{:d}-padding".format(self.grid_padding)
        ])
        grid = html.Div(
            children=self.children,
            className=grid_class,
            id=self._id,
        )
        return html.Div(
            className="dui-grid-wrapper",
            children=grid)
