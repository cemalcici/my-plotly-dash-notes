# Histgoram - Stün Grafiği
# Sütun grafiği sayısal değişkenlerin dağılımını görselleştirmek için kullanılır.
# Sütun grafiği üretildiğinde belirtilen aralığa göre sayısal değişken serisini bölümleyerek oluşturabiliriz.
# Söz konusu aralıklara "bin" adı verilir. Biz bu aralıklara göre toplam sayıları tutacağız.
# Bu "bin" değerleri değiştirilebilir.
# Sütun grafiğinin x ekseninde aralık değerleri vardır. y ekseninde ise bu aralığa düşen değerlerin toplam sayısı

# Örneğin elimizdeki veri setinin minimum değeri 9, maksimum değeri 45 olsun ve bin değerimiz 10 olsun
# Buna bağlı olarak x eksenindeki aralık listemiz [0, 10, 20, 30, 40, 50] olur.
# y eksenindeki değerler ise bu söz konusu aralık değerlerine düşen sayıların sayısını verir.
# Histogram bar chart'a benziyor olsa bile histogram sayısal seriler üzerinde gerçekleştirilir.

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("../00-data/mpg.csv")

data = [go.Histogram(x=df["mpg"])]
layout = go.Layout(title="Histogram")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="histogram1.html")
