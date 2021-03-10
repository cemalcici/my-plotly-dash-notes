import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

df1 = pd.read_csv("data/2010SitkaAK.csv")
df2 = pd.read_csv("data/2010SantaBarbaraCA.csv")
df3 = pd.read_csv("data/2010YumaAZ.csv")

data = []
for df in [df1, df2, df3]:
    trace = go.Heatmap(x=df["DAY"],
                       y=df["LST_TIME"],
                       z=df["T_HR_AVG"].values.tolist(),
                       colorscale="Jet",
                       zmin=5, # z değerinin en küçük değeri
                       zmax=40) # z değerinin en büyük değeri
    data.append(trace)

# make_subplots metodu tek bir görsel içerisine birden fazla grafik eklemek için kullanılan metottur.
fig = tools.make_subplots(rows=1, # eklenecek görselin satır sayısı
                          cols=3, # eklenecek görselin sütun sayısı
                          subplot_titles=["Sitka AK", "SB CF", "Yuma AZ"], # her bir grafiğin başlığı
                          shared_yaxes=True) # y ekseni ortak olması durumu

# yukarıda oluşturulan görsele tek tek grafik ekleniyor.
fig.append_trace(data[0], 1, 1)
fig.append_trace(data[1], 1, 2)
fig.append_trace(data[2], 1, 3)

# Genel grafiği güncellemek için
fig["layout"].update("Temp for 3 cities")

pyo.plot(fig, "heatmap4.html")
