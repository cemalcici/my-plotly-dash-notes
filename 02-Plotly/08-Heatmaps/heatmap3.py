import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/2010YumaAZ.csv")

data = [go.Heatmap(x=df["DAY"],
                   y=df["LST_TIME"],
                   z=df["T_HR_AVG"].values.tolist(), # z ekseni python listesi istediği için dönüşüm yaptık.
                   colorscale="Jet")] # reklendirme kodları için dökümantasyona bakabilirsin.

layout = go.Layout(title="SB CA Temps")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="heatmap3.html")