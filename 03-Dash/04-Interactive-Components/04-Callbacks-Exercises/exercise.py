#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:

app.layout = html.Div([
    dcc.RangeSlider(id="slider-num",
                    marks={i: i for i in range(-5, 7)},
                    min=-5,
                    max=6,
                    step=1,
                    value=[-2, 4]),
    html.H1(id="show-multiply")
], style={"padding": 20})

@app.callback(
    Output(component_id="show-multiply", component_property="children"),
    [Input(component_id="slider-num", component_property="value")]
)
def multiply(numbers):
    return numbers[0] * numbers[1]

if __name__ == "__main__":
    app.run_server()