# Line Charts (Çizgi Grafiği)
# Scaater Plot'a benzerdir.
# Buradaki tek fark her bir noktaların bir çizgi aracılığı ile birleştirilmesiyle oluşur.
# Bu değerler çizgiler aracılığı ile yatay eksen (x ekseni) üzerinde birleştirilir ve bu değerlerin çoğunlukla bir sırası vardır.
# Zaman serileri gibi trend bazlı serilerde kullanılır.

# lines --> Çizgi olarak birleştirme
# lines+markers --> Çizgi olarak birleştirme ve veri noktalarını belirtme
# markers --> Sadece veri noktaları belirtme

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Rassallığı sabitledik
np.random.seed(42)

# Ragele değerler ürettik
x_values = np.linspace(0,1, 100) # 0-1 arası 100 değer üret
y_values = np.random.randn(100) # Standart normal dağılıma göre 100 değer üret

# Her bir grafiği ara değikene atıyoruz (eğitmen bunlara trace adı verdi)
trace0 = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode='markers', # scatter plot için marker
                    name='mymarkers') # kırılım ismi (özlleştirilebilir)

trace1 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines', # line chart için lines
                    name='mylines') # kırılım ismi (özlleştirilebilir)

trace2 = go.Scatter(x=x_values,
                    y=y_values-5,
                    mode='lines+markers', # line chart için lines+markers (sık kullanılır)
                    name='mylines+markers') # kırılım ismi (özlleştirilebilir)

# Grafikleri listede birleştir.
data = [trace0, trace1, trace2] # Aynı figür içerisinde birden fazla grafik kullanabiliriz.

# Arayüz düzenle
layout = go.Layout(title="Line Charts")

# Figür olarak birleştir
fig = go.Figure(data=data, layout=layout)

# HTML olarak bas
pyo.plot(fig, filename="line-charts-1.html")