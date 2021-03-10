import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("../00-data/mpg.csv")

data = [go.Histogram(x=df["mpg"],
                     xbins=dict(start=0,
                                end=50,
                                size=10))]

# xbins: Bin işlemini temsil eder.
# start: Bin işleminin yapılması istenen ilk değer
# end: Bin işleminin yapılması istenen son değer
# size: Bin işleminin parça sayısı

layout = go.Layout(title="Histogram")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="histogram2.html")
