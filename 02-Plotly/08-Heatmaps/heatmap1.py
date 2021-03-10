# Heatmaps -> Isı Grafiği
# Heatmap 3 değişkeni bir arada görselleştiren bir görselleştirme tekniğidir.
# x ekseni ve y ekseninde sayısal değişkenler veya kategorik değişkenler yer alabilirken
# her bir hücrede ise sayısal değerler yer almaktadır.
# Burada amaç değerleri ısılama yöntemi ile görselleştirmek.

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/2010SantaBarbaraCA.csv")

data = [go.Heatmap(x=df["DAY"],
                   y=df["LST_TIME"],
                   z=df["T_HR_AVG"].values.tolist())] # z ekseni python listesi istediği için dönüşüm yaptık.

layout = go.Layout(title="SB CA Temps")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="heatmap.html")