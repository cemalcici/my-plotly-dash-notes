import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# veri setinin yüklenmesi
df = pd.read_csv("../00-data/nst-est2017-alldata.csv")

# veri manipülasyonu
df2 = df[df["DIVISION"] == "1"]  # New England olan değerleri getir.
df2.set_index("NAME", inplace=True)  # NAME değişkeni index ismi olsun.
list_of_pop_col = [col for col in df2.columns if col.startswith("POP")]  # POP ile başlayan sütun isimlerini getir.
df2 = df2[list_of_pop_col] # görselleştirecek df'i oluştur.

# List compherension yapısı ile grafik oluşturma:
data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode="lines",
                   name=name) for name in df2.index]

# Figure oluşturmadan grafik oluşturma:
pyo.plot(data, filename="line-charts-2.html")
