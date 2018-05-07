from dash import Dash
import dash_html_components as html
import dash_ui as dui

app = Dash()
my_css_urls = ["https://codepen.io/rmarren1/pen/mLqGRg.css"]

for url in my_css_urls:
    app.css.append_css({
        "external_url": url
    })

grid = dui.Grid(grid_id="grid", num_rows=12, num_cols=12, grid_padding=0)

grid.add_element(col=1, row=1, width=3, height=4, element=html.Div(
    style={"background-color": "red", "height": "100%", "width": "100%"}
))

grid.add_element(col=4, row=1, width=9, height=4, element=html.Div(
    style={"background-color": "blue", "height": "100%", "width": "100%"}
))

grid.add_element(col=1, row=5, width=12, height=4, element=html.Div(
    style={"background-color": "green", "height": "100%", "width": "100%"}
))

grid.add_element(col=1, row=9, width=9, height=4, element=html.Div(
    style={"background-color": "orange", "height": "100%", "width": "100%"}
))

grid.add_element(col=10, row=9, width=3, height=4, element=html.Div(
    style={"background-color": "purple", "height": "100%", "width": "100%"}
))

app.layout = html.Div(grid.get_component(), style={
    "height": "calc(100vh - 20px)",
    "width": "calc(100vw - 20px)"
})

if __name__ == "__main__":
    app.run_server(debug=True)
