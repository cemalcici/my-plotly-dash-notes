import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# Daha fazlası için dökümantasyona bakabilirsin:
# https://dash.plotly.com/dash-core-components

app.layout = html.Div([
    # Açılır menü oluşturma
    html.Div([
        html.Label("Dropdown"),
        dcc.Dropdown(options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "San Francisco", "value": "SF"}
        ],
                     value="SF")
    ]),
    # Aralık çubuğu oluşturma
    html.Div([
        html.Label("Slider"),
        dcc.Slider(min=-10,
                   max=10,
                   step=0.5,
                   value=0,
                   marks={i: i for i in range(-10,11, 1)})
    ]),
    # Radio Buton oluşturma
    html.Div([
        html.P(html.Label("Some Radio Items")), # TODO Buradaki sorunu araştır.
        dcc.RadioItems(options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "San Francisco", "value": "SF"}
        ],
                       value="SF")
    ])
])

if __name__ == "__main__":
    app.run_server()