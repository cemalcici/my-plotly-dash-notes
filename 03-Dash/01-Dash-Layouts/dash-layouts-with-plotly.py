import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Veri Üretme
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Plotly kullanarak grafik oluşturma
# Birinci grafik objesi
data1 = [go.Scatter(x=random_x,
                    y=random_y,
                    mode="markers",
                    marker={
                        "size": 12,
                        "color": "rgb(51,204,153)",
                        "symbol": "pentagon",
                        "line": {"width": 2}
                    })]

# İkinci grafik objesi
data2 = [go.Scatter(x=random_x,
                    y=random_y,
                    mode="markers",
                    marker={
                        "size": 12,
                        "color": "rgb(200,204,53)",
                        "symbol": "pentagon",
                        "line": {"width": 2}
                    })]

# Plotly kullanarak grafik arayüzünü hazırlama
# Birinci grafiğin layout yapısı
layout1 = go.Layout(title="My Scatterplot",
                    xaxis= {"title": "Some X Title"})

# İkinci grafiğin layout yapısı
layout2 = go.Layout(title="Second Plot",
                    xaxis= {"title": "Some X Title"})

# Dashboard'a tanımlama
app.layout = html.Div(children=[# Birinci grafik
                                dcc.Graph(id="scatterplot",
                                          figure={"data": data1,
                                                  "layout": layout1}),
                                # İkinci grafik
                                dcc.Graph(id="scatterplot2",
                                          figure={"data": data2,
                                                  "layout": layout2})])

if __name__ == "__main__":
    app.run_server()