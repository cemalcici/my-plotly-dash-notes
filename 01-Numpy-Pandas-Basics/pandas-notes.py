import pandas as pd
import numpy as np

# Veri seti ile işlemler
df = pd.read_csv('salaries.csv')
print(df) # df yazdırma
print()
print(df["Salary"]) # bir sütun yazdırma
print()
print(df[["Name", "Salary"]]) # birden fazla sütun yazdırma
print()
print(df["Salary"].min()) # bir sütunun min değerini bulma
print()
print(df["Salary"].mean()) # bir sütunun max değerini bulma
print()
print(df["Age"] > 30) # boolean serisi oluşturma
print()
print(df[df["Age"] > 30]) # koşullu eleman seçme
print()
print(df["Age"].unique()) # sütuna ait eşsiz değerleri bulma
print()
print(df["Age"].nunique()) # sütuna ait eşsiz değerlerin sayısını bulma
print()
print(df.columns) # sütun isimlerini getirme
print()
print(df.info()) # veri seti ile ilgili metaveri
print()
print(df.describe()) # tanımlayıcı istatistikler
print()
print(df.index) # satır isimlerini getirme
print()

# Veri Üretme
mat = np.arange(0, 50).reshape(5, 10) # numpy kullanılarak veri üretildi 5x10
df = pd.DataFrame(data=mat) # df'e çevrildi
print(df)
print()
mat = np.arange(0, 10).reshape(5, 2) # 5x2
df = pd.DataFrame(data=mat, columns=["A", "B"]) # sütun isimleri ile atandı
print(df)