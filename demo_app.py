import dash
import dash_ui as dui

app = dash.Dash()
grid = dui.Grid(grid_id="my-grid", num_rows=12, num_cols=12)
app.layout = grid.get_component()

if __name__ == '__main__':
    app.run_server(debug=True)
