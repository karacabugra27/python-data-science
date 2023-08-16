
import pandas as pd

s = pd.Series([10, 77, 22, 15, 64])

#index bir iç özellik
#ekonomik ve zamana yönelik bir kütüphane

type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3) #istenen kadar veri getirir
s.tail(3) #sondan veri getirir

## VERİYE HIZLI BAKIŞ

import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].value_counts()

#pandasta veri seçim işlemleri ( selection in pandas)

df.index
df[0: 13]
df.drop(0, axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0, inplace=True) # inplace metodu kalıcı hale getirir.

# değişkeni indexe çevirmek

df["age"].head()
df.age.head()

df.index = df["age"]
df.drop("age", axis=1, inplace= True)
df.head()

# indexi değişkene çevirmek

df.index

df["age"] = df.index

df.head()

df.reset_index().head()
df = df.reset_index()
df.head()


# değişken üzerinde işlemler

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

type(df.[["age"]].head())

    ##iloc ve loc

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

#iloc integer based location

df.iloc[0: 3]
df.iloc[0, 0]

df.loc[0: 3, "age"]

dfset = ["age", "alive" ,"sex"]

df.loc[0:5, dfset]


## KOŞULLU SEÇİM

df[df["age"]>50].head()
df[df["age"]>50]["age"].count()

df_new = df.loc[(df["age"]>50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Southampton") | (df["embark_town"] == "Cherbourg")), ["age", "class", "embark_town"]]

## toplulaştırma ve gruplama

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()
df["age"].mean()


df.groupby("sex")["age"].mean()

df.groupby(["sex", "embark_town", "class"]).agg(
    {"age": ["mean"]
    ,"survived": ["mean"]
    ,"sex": "count"})

    #pivot table

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df["new_age"] = pd.cut(df["age"],[0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "new_age", "sex")

##APPLY VE LAMBDA

# apply : döngülerden daha pratik satır veya sütunlarda otomatik olarak çalışan
# lambda : fonksiyon kullanmadan kullan at fonksiyonlardır


import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"] * 5
df["age3"] = df["age"] * 10

df[["age", "age2", "age3"]].apply(lambda x : x/10).head()

df.loc[: , df.columns.str.contains("age")].apply(lambda x : x - x.mean() / x.std() ).head()

def scaler(col_name):
    return(col_name - col_name.mean() / col_name.std())

df.loc[: , df.columns.str.contains("age")].apply(scaler).head()

# JOİN İŞLEMLERİ (BİRLEŞTİRME)

import numpy as np
import pandas as pd
m = np.random.randint(1, 30, (5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
## DataFrame sıfırdan dataframe oluşturmaya yarar
df2 = df1 + 99

pd.concat([df1, df2])
# indexler resetlenmeyip tekrardan 0 dan başladı

pd.concat([df1, df2], ignore_index = True)

# indexler sıralandı

#merge ile birleştirme işlemleri

# daha detaylı birleştirme imkanı sağlar

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2= pd.DataFrame({"employees": ["mark", "john", "maria", "dennis"],
                   "start_date": [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)

# neye göre birleşmesini belirtmek için

df3 = pd.merge(df1, df2, on="employees")

# amaç : her çalışanın müdür bilgisine erişmek için

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3, df4, on = "group")

