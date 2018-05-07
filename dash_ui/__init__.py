import dash_html_components as html
import dash_core_components as dcc


class Grid:
    def __init__(self, grid_id="default_grid_id",
                 children=[], num_rows=1, num_cols=1):
        self.className = "dgg-grid"
        self.children = children
        self.grid_id = grid_id
        self.num_rows = num_rows
        self.num_cols = num_cols

    def add_graph(self, graph_id, col, row, width, height):
        self.children.append(html.Div(
            style={
                "grid-column": "{:%d} / span {:%d}".format(col, width),
                "grid-row": "{:%d} / span {:%d}".format(row, height)
            },
            children=dcc.Graph(id=graph_id, className="dgg-grid-figure")
        ))

    def get_component(self):
        rows = ["{:.4f}%".format(100 / self.num_rows)] * self.num_rows
        cols = ["{:.4f}%".format(100 / self.num_cols)] * self.num_cols
        return html.Div(
            className="dgg-grid-wrapper",
            style={'height': '100vh',
                   'width': '100vw'},
            children=html.Div(
                children=self.children,
                className=self.className,
                id=self.grid_id,
                style={
                    'display': 'grid',
                    'height': '100%',
                    'width': '100%',
                    'grid-template-rows': rows,
                    'grid-template-columns': cols
                }))
