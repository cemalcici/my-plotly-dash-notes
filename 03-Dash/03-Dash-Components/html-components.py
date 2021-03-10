# Dash HTML Components
import dash
import dash_html_components as html

app = dash.Dash()

# Daha fazlası için dökümantasyona bakabilirsin
# https://dash.plotly.com/dash-html-components

app.layout = html.Div(["This is the outermost div!",
                       html.Div("This is an inner div!",
                                style={"color": "red",
                                       "border": "2px red solid"}),
                       html.Div(["Another inner div"],
                                 style={"color": "blue",
                                        "border": "3px blue solid"})],
                      style={"color": "green",
                             "border": "2px green solid"})

if __name__ == "__main__":
    app.run_server()