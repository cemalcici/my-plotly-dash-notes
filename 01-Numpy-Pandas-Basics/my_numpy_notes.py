# Numpy

# Bilimsel hesaplamalarda kullanılan bir kütüphanedir.
# Bu eğitimde rassla diziler ve matrisler oluşturmak için NumPy kullanılacaktır.

import numpy as np

# Listeden dizi oluşturma
mylist = [1, 2, 3, 4] # list
print(np.array(mylist))
print(type(mylist))
arr = np.array(mylist) # numpy array
print(type(arr))

# Array oluşturma metotları

# np.arange() --> range fonksiyonuna benzer.
a = np.arange(0,10)  # 0'dan 10'a kadar sayı üretir (10 dahil değil)
print(a)
a = np.arange(0,10, 2) # 0'dan 10'a kadar 2 adımlı sayı üretir (10 dahil değil)
print(a)

# np.zeros() --> Belirtilen boyutlarda 0 değerleri üretir.
a = np.zeros(5)  # 5 elemanlı 0 değerleri üretir.
print(a)
a = np.zeros((5, 5)) # 5x5 elemanlı 0 değerleri üretir.
print(a)

# np.ones() --> Belirtilen boyutlarda 1 değerlerini üretir.
a = np.ones(10) # 10 elemanlı 1 değerleri üretir.
print(a)
a = np.ones((2, 4)) # 2x4 elemanlı 1 değerileri üretir.
print(a)

# np.random.randint() --> Uniform dağımına göre rasgele sayı üreetir.
np.random.randint(0, 100) # 0-100 arası (ikisi de dahil olacak şekilde) rasgele sayu üretir
np.random.randint(0, 100, (5, 5)) # rasgele sayılardan 5x5 matrisi oluştur oluştur.

# np.linspace() --> Başlangıç değerinden bitiş değerine kadar belirtilen sayı kadar değer üretir.
np.linspace(0, 10, 6)
np.linspace(0, 10, 101)

# np.random.seed() --> Rasgele üretilen değerleri sabitlemek için kullanılan bir sabitleyici.
np.random.seed(101) # Eğitim boyunca kullanacağız.
np.random.randint(0, 100, 10)

arr = np.random.randint(0, 100, 10)
print(arr)
arr.max() # dizideki maksimum değer
arr.min() # dizideki minimum değer
arr.mean() # dizinin ortalama değeri
arr.argmax() # dizideki maksimum değerin indeksi
arr.argmin() # dizideki minimum değerin indeksi
arr.reshape(2, 5) # dizinin boyutunu değiştirmek için kullanılır

# Eleman seçme
mat = np.arange(0, 100).reshape(10, 10)
print(mat)
mat[5, 2] # 6. satr ve 3. sütun seçme
mat[:, 2] # 3. sütuna ait bütün satırları seçme
mat[2, :] # 3. satıra ait bütün sütunları seçme

# Koşullu eleman seçme
mat > 50 # 50'den büüyük olan bütün değerleri sorgula
mat[mat > 50] # 50'den büüyük olan bütün değerleri yazdır
