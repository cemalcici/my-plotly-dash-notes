import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1(id="live-update-text"),
    dcc.Interval(id="interval-component",
                 interval=2000,
                 n_intervals=0)
])


@app.callback(Output("live-update-text", "children"),
              [Input("interval-component", "n_intervals")])
def update_layout(n):
    return f"Crash free for {n} refreshes."


if __name__ == "__main__":
    app.run_server()