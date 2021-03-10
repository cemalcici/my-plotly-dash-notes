# Box Plot - Kutu Grafiği

# Kutu grafiği, sürekli numerik değişkenleri çeyrekliklere bölen grafiktir.
# Kategorik değişken kırılımında sürekli numerik değişkenlerin çeyreklikleri incelenebilir.
# Kutu grafiği, değişken dağılımını çeyrekliklere göre görselleştiren bir grafiktir.
# Çeyreklikler, veri setini 4 eşit parçaya bölen değerlerdir.
# Bir kutu grafiği bir değişkene ait aykırı değerleri görmemizi sağlamaktadır.

import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

# Verilerin dağılımı ile birlikte kutu grafiğini göster
data = [
    go.Box(
        y=y,
        boxpoints='all', # display the original data points
        jitter=0.3,      # spread them out so they all appear
        pointpos=-1.8    # offset them to the left of the box
    )
]

pyo.plot(data, filename='boxplot1.html')
