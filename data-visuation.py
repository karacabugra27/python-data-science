#######################################################
###### MATPLOTLIB & SEABORN ( VERİ GÖRSELLEŞTİRME ) ###
#######################################################

#######################################################
# MATPLOTLIB : low-level veri görselleştirme aracıdır, atalarıdır.
#######################################################

# kategorik değişken varsa sütunla ya da pasta
# ( seaborn : countplot) ( matplotlib : barplot )

# sayısal değişken varsa
# histogram ve boxplot
# ikisi de dağılım gösterir ( boxplot aykırı değerleri de gösterir )

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", 25)
pd.set_option("display.max_columns", 5)
pd.set_option("display.width", 300)

df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind = "bar")
plt.show()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

#######################################################
# plot
#######################################################

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show()

#######################################################
# marker
#######################################################

y = np.array([13, 25, 33, 53, 77])

plt.plot(y, marker = "o")
plt.show()

#######################################################
# line, multiple lines
#######################################################

x = np.array([23, 15, 5, 44])
y = np.array([13, 25, 33, 53, 77])

plt.plot(y, linestyle = "dashdot", color = "red")
plt.plot(x, linestyle = "dotted", color = "blue")
plt.show()

#######################################################
# labels
#######################################################

x = np.array([23, 15, 5, 44, 99])
y = np.array([13, 25, 33, 53, 77])

plt.plot(x, y)

plt.title("ana başlık")

plt.xlabel("x başlığı")
plt.ylabel("y başlığı")
plt.grid()
plt.show()

#######################################################
# subplots : birden fazla görselin gösterilmesi
#######################################################

x = np.array([23, 15, 5, 44, 99])
y = np.array([13, 25, 33, 53, 77])

plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)
plt.show()

x = np.array([44, 55, 77, 84, 99])
y = np.array([3, 15, 23, 43, 67])

plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


#################################################
################# SEABORN #######################
#################################################

df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x = df["sex"], data= df)
plt.show()

##################################################
######## SAYISAL DEĞİŞKENLERİ GÖSTERME############
##################################################

sns.boxplot(x = df["total_bill"])
plt.show()

#pandas fonksiyonu hist

df["total_bill"].hist()
plt.show()













































