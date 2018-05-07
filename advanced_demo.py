from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_ui as dui
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

app = Dash()
my_css_urls = [
  "https://codepen.io/rmarren1/pen/mLqGRg.css",
]

for url in my_css_urls:
    app.css.append_css({
        "external_url": url
    })

grid = dui.Grid(grid_id="grid", num_rows=12, num_cols=12, grid_padding=5)

grid.add_graph(col=1, row=1, width=3, height=4, graph_id="all-pie")

grid.add_graph(col=4, row=1, width=9, height=4, graph_id="all-bar")

grid.add_graph(col=1, row=5, width=4, height=4, graph_id="produce-pie")

grid.add_element(
    col=5, row=5, width=4, height=4,
    element=html.Div([
        html.H1("Dash UI Grid: US Agriculture Example"),
        html.H3("Choose a State"),
        dcc.Dropdown(
            id="state-dropdown",
            options=[{'label': x.title(), 'value': x}
                     for x in df["state"].tolist()],
            value=df["state"].tolist()[0])
        ], style={
            "background-color": "Azure",
            "border-radius": "5px",
            "height": "100%",
            "width": "100%",
            "padding": "2px",
            "text-align": "center"})
    )

grid.add_graph(col=9, row=5, width=4, height=4, graph_id="animal-pie")

grid.add_graph(col=1, row=9, width=9, height=4, graph_id="total-exports-bar")

grid.add_graph(col=10, row=9, width=3, height=4, graph_id="total-exports-pie")


app.layout = html.Div(grid.get_component(), style={
    "height": "calc(100vh - 20px)",
    "width": "calc(100vw - 20px)"
})


@app.callback(Output('total-exports-pie', 'figure'),
              [Input('state-dropdown', 'value')])
def create_total_exports_pie(state):
    trace = go.Pie(
        labels=df['state'],
        values=df['total exports'],
        textinfo='none',
        marker=dict(
            colors=['red' if x == state else 'grey' for x in df['state']]
        ))
    return go.Figure(data=[trace], layout={
        'showlegend': False,
        'title':
        "{:s}'s proportion of total US agriculture exports".format(state)
    })


@app.callback(Output('total-exports-bar', 'figure'),
              [Input('state-dropdown', 'value')])
def create_total_exports_bar(state):
    my_df = df.sort_values('total exports', ascending=False)
    trace = go.Bar(
        x=my_df['state'],
        y=my_df['total exports'],
        marker=dict(
            color=['red' if x == state else 'grey' for x in my_df['state']]
        ))
    return go.Figure(data=[trace], layout={
        'showlegend': False,
        'title':
        "{:s}'s agriculture exports vs. other states".format(state)
    })


@app.callback(Output('produce-pie', 'figure'),
              [Input('state-dropdown', 'value')])
def create_produce_pie(state):
    produce_vars = ["total fruits", "total veggies", "corn", "wheat"]
    row = df[df["state"] == state].iloc[0]
    trace = go.Pie(
        labels=produce_vars,
        textinfo="label+percent",
        values=[row[v] for v in produce_vars])
    return go.Figure(data=[trace], layout={
        'showlegend': False,
        'title':
        "{:s}'s produce distribution".format(state)
    })


@app.callback(Output('animal-pie', 'figure'),
              [Input('state-dropdown', 'value')])
def create_animal_pie(state):
    animal_vars = ["beef", "pork", "poultry", "dairy"]
    row = df[df["state"] == state].iloc[0]
    trace = go.Pie(
        labels=animal_vars,
        textinfo="label+percent",
        values=[row[v] for v in animal_vars])
    return go.Figure(data=[trace], layout={
        'showlegend': False,
        'title':
        "{:s}'s animal product distribution".format(state)
    })


@app.callback(Output('all-pie', 'figure'),
              [Input('state-dropdown', 'value')])
def create_all_pie(state):
    vs = list(set(df.columns) - {"Unnamed: 0", "total exports", "state"})
    row = df[df["state"] == state].iloc[0]
    trace = go.Pie(
        labels=vs,
        textinfo="label+percent",
        values=[row[v] for v in vs])
    return go.Figure(data=[trace], layout={
        'showlegend': False,
        'title':
        "{:s}'s agriculture distribution".format(state)
    })


@app.callback(Output('all-bar', 'figure'),
              [Input('state-dropdown', 'value')])
def create_all_bar(state):
    vs = list(set(df.columns) - {"Unnamed: 0", "total exports", "state"})
    row = df[df["state"] == state].iloc[0]
    trace = go.Bar(
        x=vs,
        y=[row[v] for v in vs])
    return go.Figure(data=[trace], layout={
        'showlegend': False,
        'title':
        "{:s}'s agriculture distribution".format(state)
    })
if __name__ == "__main__":
    app.run_server(debug=True)
