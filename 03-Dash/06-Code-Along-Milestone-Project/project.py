import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas_datareader.data as web
import pandas as pd
from datetime import datetime
from dash.dependencies import Input, Output, State


app = dash.Dash()

nsdq = pd.read_csv("NASDAQcompanylist.csv")
nsdq.set_index("Symbol", inplace=True)
options = [{"label": f"{nsdq.loc[tic, 'Name']} {tic}", "value": tic} for tic in nsdq.index]


app.layout = html.Div([
    html.H1("Stock Ticker Dashboard", style={"paddingRight": "30px"}),
    html.Div([
        html.H3("Enter a stock symbol: "),
        dcc.Dropdown(id="my-stock-picker",
                     options = options,
                     value=["GE"],
                     multi=True)
    ], style={"display": "inline-block", "verticalAlign": "top", "width": "30%"}),
    html.Div([
        html.H3("Select a start and end date: "),
        dcc.DatePickerRange(id="my-date-picker",
                            min_date_allowed=datetime(2015,1,1),
                            max_date_allowed=datetime.today(),
                            start_date=datetime(2021, 1, 1),
                            end_date=datetime.today())
    ], style={"display": "inline-block"}),
    html.Div([
        html.Button(id="submit-button",
                    n_clicks=0,
                    children="Submit",
                    style={"fontSize": 24, "marginLeft":"30px"})
    ], style={"display": "inline-block"}),
    dcc.Graph(id="my-graph",
              figure={"data": [{"x": [1, 2], "y": [3, 1]}],
                      "layout": {"title": "Default Title"}})
])


@app.callback(Output("my-graph", "figure"),
              [Input("submit-button", "n_clicks")],
              [State("my-stock-picker", "value"),
               State("my-date-picker", "start_date"),
               State("my-date-picker", "end_date")])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    # yukarıda datetime objesi olarak tanımlanıyor ancak girdi alındığında
    # str yapısına sahip oluyor. Bu yüzden tarihleri yeniden formatlıyoruz
    start = datetime.strptime(start_date[:10], "%Y-%m-%d")
    end = datetime.strptime(end_date[:10], "%Y-%m-%d")
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic, "yahoo", start, end)
        traces.append({"x": df.index, "y": df.Close, "name": tic})
    fig = {"data": traces,
           "layout": {"title": stock_ticker}}
    return fig


if __name__ == "__main__":
    app.run_server()