# Bar Charts --> Sütun Grafiği
# Kategorik değişkenleri sütunlar ile görselleştiren bir yöntemdir.
# Kategorik değişkenleri belirli bir orana göre temsil eder.

# Genellikle veriler ölçülebilir bir yapıya sahipler ise sürekli ölçek kullanılır. Örneğin yaş, genişlik ve uzunluk.
# Genellikle veriler bilgi barındırıyor ise kategorik veya kesikli özniteliktir. Örneğin cinsiyet

# Sütun grafik ile biz kategorik değişkenleri görselleştirebiliriz.
# Genel olarak x ekseninde kategoriler bulunurken y ekseninde ise kategorilerin görülme sıklıkları yer alır.
# y ekseninde herhangi bir toplulaştırma değerleri de kullanılabilir (toplam, ortalama, vs.)

# Stacked Bar Chart --> Yığın Sütun Grafiği
# Kategorik değişkenler içerisinde başka kategorik kırılımlar oluşturmak için yığın sütun grafiği gereklidir.
# Bu kırılımlar tek sütun üzerinde yığınlaştırılmış şekilde oluşturulur.
# Genellikle yığınların toplamını bulmak için kullanılır.

# Nested Bar Chart --> İç İçe Sütun Grafiği
# Kategorik değişkenler içerisinde başka kategorik kırılımlar oluşturmak için yığın sütun grafiği gereklidir.
# Bu kırılımlar kırılım kategorileri kadar yan yana sütunlar kullanılarak oluşturulur.
# Genellikle kırılımların sayılarını tespit etmek için kullanılır.

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../00-data/2018WinterOlympics.csv')
print(df)

trace1 = go.Bar(x=df["NOC"],
                y=df["Gold"],
                name="Gold",
                marker=dict(color="#FFD700"))

trace2 = go.Bar(x=df["NOC"],
                y=df["Silver"],
                name="Silver",
                marker=dict(color="#9EA0A1"))

trace3 = go.Bar(x=df["NOC"],
                y=df["Bronze"],
                name="Bronze",
                marker=dict(color="#CD7F32"))

data = [trace1, trace2, trace3]  # nested bar charts

# Tek sütun grafik
# data = [go.Bar(x=df["NOC"],
#              y=df["Total"])]

# layout = go.Layout(title="Medals") # nested barcharts için bu şekilde kullanılıyor
layout = go.Layout(title="Medals", barmode="stack")  # stack bar chart için bu şekilde kullanılıyor
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="bar-charts-1.html")
