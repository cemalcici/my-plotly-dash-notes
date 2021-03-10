#######
# Objective: 2010YumaAZ.csv dosyasını kullanarak bir Line Chart geliştir.
# x ekseninde gün içerisindeki saatler yer alırken,
# y ekseninde ise sıcaklık değeri yer almakta.
# Buradaki amaç günler bazında zamana bağlı sıcaklık değişimini gösteren bir çizgi grafiği oluşturmak.
######

# Kütüphanelerin yüklenmesi
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# 2010YumaAZ.csv dosyasını kullanarak bir df oluştur
df = pd.read_csv("../00-data/2010YumaAZ.csv")
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# for döngüsü kullanarak grafikleri oluştur (list comp kullanmak da bir seçenek)
data = []
for day in days:
    trace = go.Scatter(x=df["LST_TIME"],
                       y=df.loc[df["DAY"] == day, "T_HR_AVG"],
                       mode="lines",
                       name=day)
    data.append(trace)

# List comp ile
# data = [go.Scatter(x=df["LST_TIME"],
#                    y=df.loc[df["DAY"] == day, "T_HR_AVG"],
#                    mode="lines",
#                    name=day) for day in days]

# Arayüz tanımla
layout = go.Layout(title="Daily temperatures from June 1-7, 2010 in Yuma, Arizona",
                   hovermode="closet")

# Figür oluştur
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="line-charts-3.html")
