# Bubble Charts - Baloncuk Grafiği

# Baloncuk Grafiği saçılım grafiğine benzer ancak ondan farklı olarak üçüncü bir değişkene sahiptir:
# Noktanın büyüklüğü. Bu noktalar kategorik değişkenlere göre de renklendirilebilir.

# Normalde saçılım grafiğinde noktanın büyüklüğü sabitti ancak baloncuk grafiğinde noktanın büyüklüğü
# Veride belirtilen kırılıma göre belirlenebiliyor.

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/mpg.csv")
# print(df)
# print(df.columns)

# Bu bölümde kullanılan baloncuk grafiği cylinders kırılımında
# horsepower ve mpg değişkenleri arasındaki ilişkiyi göstermektedir.

# data = [go.Scatter(x=df["horsepower"],
#                    y=df["mpg"],
#                    text=df["name"],
#                    mode="markers",
#                    marker=dict(size=2 * df["cylinders"]))] # 2 ile çarpılmasının sebebi daha büyük görünmesi için

# data = [go.Scatter(x=df["horsepower"],
#                    y=df["mpg"],
#                    text=df["name"],
#                    mode="markers",
#                    marker=dict(size=df["weight"] / 100))] # 100 ile bölünmesinin sebebi büyük derğerleri büyük, küçük değerleri küçük göstersmesi için

# data = [go.Scatter(x=df["horsepower"],
#                    y=df["mpg"],
#                    text=df["name"],
#                    mode="markers",
#                    marker=dict(size=df["weight"] / 100, # numerik kırılım
#                                color=df["cylinders"]))] # kategorik kırılım

data = [go.Scatter(x=df["horsepower"],
                   y=df["mpg"],
                   text=df["name"],
                   mode="markers",
                   marker=dict(size=df["weight"] / 100, # numerik kırılım
                               color=df["cylinders"], # kategorik kırılım
                               showscale=True))] # ölçek gösterildi

layout = go.Layout(title="Bubble Chart")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="bubble-charts-1.html")