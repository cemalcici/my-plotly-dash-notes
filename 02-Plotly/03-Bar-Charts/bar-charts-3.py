# bar-charts-2.py dosyası ile aynı. 14. satıra ekleme yapılmış

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv("data/mocksurvey.csv", index_col=0)

# create traces using a list comprehension:
data = [go.Bar(y=df.index,
               x=df[response],
               orientation='h',  # dikey olmasını sağlıyor
               name=response) for response in df.columns]

# create a layout, remember to set the barmode here
layout = go.Layout(title="Mock Survey", barmode='stack')

# create a fig from data & layout, and plot the fig.
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="bar-charts-3.html")
