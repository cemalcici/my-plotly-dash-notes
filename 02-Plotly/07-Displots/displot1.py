# Distplot - Dağılım Grafiği
# Dağılım grafiği sayısal serinin dağılımını veren grafiktir.
# üç katmanlı bir görsele sahiptr.
# 1. Katmanda histogram
# 2. Katmanda rug plot (araştırdığıma göre püskül grafiği) veri dağilımını püskül şeklinde görselleştirmeyi sağlar.
# 3. Katmanda kernel density estimate (KDE) çizgisi veri kümesini eğri ile görselleştirmeye yarar

import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x = np.random.randn(1000)
hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename="displot1.html")
