import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

# Sadece aykırı değerlerin gösterileceği kutu grafiğini göster
data = [go.Box(y=y,
               boxpoints="outliers")]

pyo.plot(data, filename='boxplot2.html')
