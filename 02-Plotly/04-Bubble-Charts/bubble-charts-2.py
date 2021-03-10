#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv("data/mpg.csv")

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df["displacement"],
                   y=df["acceleration"],
                   text=df["name"],
                   mode="markers",
                   marker=dict(size=df['weight']/500))]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Vehicle acceleration vs. displacement',
    xaxis = dict(title = 'displacement'),
    yaxis = dict(title = 'acceleration = seconds to reach 60mph'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="bubble-charts-2.html")