import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64 # resimleri açmak için kullanılan bir kütüphane

df = pd.read_csv("../../00-data/wheels.csv")

app = dash.Dash()

def encode_image(image_file):
    """
    Bu fonksiyonun amacı belirtilen resim yolunu açmaya yarar.
    Parameters
    ----------
    image_file str
        resim dosyasının yolunu belirtir.
    Returns
    -------
        Resmin kendisini gösterir.
    """
    encoded = base64.b64encode(open(image_file, "rb").read())
    return f"data:image/png;base64,{encoded.decode()}"

app.layout = html.Div([
    html.Div([
        dcc.RadioItems(id="wheels",
                       options=[{"label": i, "value": i} for i in df["wheels"].unique()],
                       value=df["wheels"].unique()[0]),
        html.Div(id="wheels-output")
    ]),
    html.Hr(),
    html.Div([
        dcc.RadioItems(id="colors",
                       options=[{"label": i, "value": i} for i in df["color"].unique()],
                       value=df["color"].unique()[0]),
        html.Div(id="colors-output")
    ]),
    html.Hr(),
    html.Div([
        html.Img(id="display-image", src="children", height=300)
    ])
], style={"fontFamily": "helvetica",
          "fontSize": 18})


@app.callback(
    Output(component_id="wheels-output", component_property="children"),
    [Input(component_id="wheels", component_property="value")]
)
def callback_a(wheels_value):
    """
    Teker sayısını döndüren fonksiyon
    Parameters
    ----------
    wheels_value int
        Teker sayısı

    Returns
    -------
    message str
        mesajın kendisi
    """
    return f"You Choose {wheels_value}"

@app.callback(
    Output(component_id="colors-output", component_property="children"),
    [Input(component_id="colors", component_property="value")]
)
def callback_b(colors_value):
    return f"You Choose {colors_value}"

@app.callback(
    Output(component_id="display-image", component_property="src"),
    [Input(component_id="wheels", component_property="value"),
     Input(component_id="colors", component_property="value")]
)
def callback_image(wheel, color):
    path = "../../00-data/Images/"
    return encode_image(path+df.loc[(df["wheels"] == wheel) & (df["color"] == color), "image"].values[0])

if __name__ == "__main__":
    app.run_server()
