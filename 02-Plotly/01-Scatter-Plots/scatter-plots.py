# Scatter Plots (Saçılım Grafiği)
# İki değişkene ait değerlerin ilişkisini inceler.
# Herbir x ve y koordinatlarına gelen noktaların oluşturduğu grafik bu iki değişken arasındaki korelasyonu inceler.

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Rassallığı sabitledik
np.random.seed(42)

# Rasgele x ve y değerleri oluşturduk
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Grafiğimizi oluşturduk
# plotly'de grafik tanımlamak için köşeli parantezler kullanılıyor.
data = [
    # TODO Scatter metoduna dökümantasyondan bak
    go.Scatter(x=random_x, # x değişkeni
               y=random_y, # y değişkeni
               mode='markers', # noktaların gösterilme türünü belirtiyoruz (dökümantasyondan detay bakılacak)
               marker=dict(
                   size=12, # nokta büyüklüğü
                   color='rgb(51, 204, 153)', # nokta rengi
                   symbol='pentagon', # nokta şekli
                   line={'width': 2} # nokta kenar kalınlığı
               ))
]

# Grafik üzerindeki alanlara yazılar yazdırıyoruz.
# grafik üzerinde işlemler yapabilmek için layout metodu kullanılıyor. (Dikkat! liste içerisinde oluşturulmuyor)
# TODO Layout metoduna dökümantasyondan bak
layout = go.Layout(title="Hello First Plot", # grafiğin başlığı
                   xaxis={'title': 'MY X AXIS'}, # x başlığı ve y başlığı için sözlük yapısı kullanılıyor
                   yaxis=dict(title="MY Y AXIS"), # dökümantasyonda yaygınca kullanılan bu
                   hovermode="closest") # her bir noktanın konumunun nerede görüleceğini belirler

# Grafiği ve oluşturduğumuz şablonu birleştiriyoruz
fig = go.Figure(data=data, layout=layout) # Grafiği ve grafik özelliklerini bir metotla birleştiriyoruz.

# Figürü html dosyasına basıyoruz
pyo.plot(fig, filename='scatter-plot.html')

# İlk aşamada anlaşılmasa bile aşağıdaki adımları bilmemiz yeterli:
# 1. Grafik oluştur (data değişkeni ile)
# 2. Arayüz oluştur (layout değişkeni ile)
# 3. İkisini bir figüre koy (fig değişkeni ile)
# 4. Figürü HTML dosyasına bas (pyo.plot() metodu ile)

# 1. adımda anlatılanları herbir grafik için tekrar tekrar kullanacağız. Bu yüzden pedal çevirmeye devam!
