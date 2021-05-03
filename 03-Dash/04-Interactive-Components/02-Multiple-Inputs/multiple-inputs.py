import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("../../00-data/mpg.csv")

app = dash.Dash()

# Değişken isimlerini dropdown menü için tutma
options_cols = [{"label": col, "value": col} for col in df.columns]

# Arayüzün tasarımı
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id="x-axis",
                     options=options_cols,
                     value=df.columns[0])
    ], style={"width": "48%", "display": "inline-block"}),
    html.Div([
        dcc.Dropdown(id="y-axis",
                     options=options_cols,
                     value=df.columns[1])
    ], style={"width": "48%", "display": "inline-block"}),
    dcc.Graph(id="feature-graphic")
], style={"padding": 10})

# İnteraktif Grafiğin Oluşturulması
@app.callback(
    Output(component_id="feature-graphic", component_property="figure"),
    [Input(component_id="x-axis", component_property="value"), # x değerini belirleme
     Input(component_id="y-axis", component_property="value")] # y değerini belirleme
)
def update_graph(x_axis_name, y_axis_name):
    return {"data": [go.Scatter(x=df[x_axis_name],
                                y=df[y_axis_name],
                                text=df["name"],
                                mode="markers",
                                marker={"size": 15,
                                        "opacity": 0.5,
                                        "line": {"width": 0.5,
                                                 "color": "white"}}
                                )],
            "layout": go.Layout(title="My Dashboard for MPG",
                                xaxis={"title": x_axis_name},
                                yaxis={"title": y_axis_name},
                                hovermode="closest")}

if __name__ == "__main__":
    app.run_server()