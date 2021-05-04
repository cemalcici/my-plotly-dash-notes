import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return f"data:image/png;base64,{encoded.decode()}"

app = dash.Dash()

df = pd.read_csv("../00-data/wheels.csv")

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
                    "float": "left"}),

    # sağ bölme
    html.Div(html.Img(id="hover-data", src="children", height=300),
             style={"paddingTop": "35"})
])

@app.callback(Output("hover-data", "src"),
              [Input("wheels-plot", "hoverData")])
def callback_image(hoverData):
    color = hoverData["points"][0]["x"]
    wheel = hoverData["points"][0]["y"]
    path = "../00-data/Images/"
    return encode_image(path + df[(df["wheels"] == wheel) & (df["color"] == color)]["image"].values[0])

if __name__ == "__main__":
    app.run_server()