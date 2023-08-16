
import numpy as np

np.array([1, 2, 3, 4, 5])

np.zeros(5, dtype=int)
np.random.randint(5, 15, 3)
np.random.normal(10, 3, (2,3) ) #ortalaması 10 olan standart sapması 3 olan 2 ye 3 lük bir dizi matris

#ndim: boyut sayısı
#shape : boyut bilgisi
#size :toplam eleman bilgisi
#dtype : array veri tipi

a = np.random.randint(1, 10, 5)
print(a)
a.ndim
a.shape
a.size
a.dtype



# yeniden şekillendirme ( reshaping )

ar = np.random.randint(1, 5, 10)
ar.resize(9)
ar.reshape(3, 3)

# index seçimi ( index selection )

ar[1:2]

m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1, 1]
m[:, 0]
m[0, :]
m[0:2, 0:3]

# fancy index

v = np.arange(0, 30, 3 )

v[1]

catch = [1, 2, 3]

v[catch]##fancy index

import numpy as np

t = np.array([1, 2, 3, 4, 5])

##KLASİK DÖNGÜYLE

at = []

for i in t:
    if i < 3:
        at.append(i)

print(at)

##NUMPY İLE

t < 3

t[t < 3]

np.subtract(t,1)
np.add(t,1)
np.mean(t)
np.sum(t)
np.min(t)
np.max(t)
np.var(t)


## NUMPY İLE İKİ BİLİNMEYENLİ DENKLEM

#5*x0 + x1 = 12
# x0 + 3*x1 = 10

a1 = np.array([[5, 1], [1, 3]])
a2 = np.array([12, 10])

np.linalg.solve(a1, a2)

