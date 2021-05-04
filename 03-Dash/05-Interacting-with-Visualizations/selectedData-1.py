import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

# Her grafik üzerinde gezildiğinde veri toplanabilir.

app = dash.Dash()

df = pd.read_csv("00-data/wheels.csv")

app.layout = html.Div([
    # sol bölme
    html.Div(dcc.Graph(id="wheels-plot",
                       figure={"data": [go.Scatter(x=df["color"],
                                                   y=df["wheels"],
                                                   dy = 1,
                                                   mode="markers",
                                                   marker={"size": 15})],
                               "layout": go.Layout(title="Test",
                                                   hovermode="closest")}),
             style={"width": "30%",
                    "display": "inline-block"}),

    # sağ bölme
    html.Div(html.Pre(id="selection", style={"paddingTop": 35}),
             style={"width": "30%",
                    "display": "inline-block",
                    "verticalAlign": "top"})
])

@app.callback(Output("selection", "children"),
              [Input("wheels-plot", "selectedData")])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)

if __name__ == "__main__":
    app.run_server()