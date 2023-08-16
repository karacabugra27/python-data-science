import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() for col in df.columns]
#büyük harf yapma

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns ]

#görev 2

df = sns.load_dataset("car_crashes")
df.columns


df.columns = [col.upper() if "NO" in col else col.upper() + "_FLAG" for col in df.columns]


#görev 3

og_list = {"abbrev", "no_previous"}

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]

new_df.head()

#pandas alıştırmalar
#1
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.shape

#2
df["sex"].value_counts()

#3
df.nunique()
#unique değerleri ve sayılarına ulaşabiliyoruz

#4
df["pclass"].unique()

#5
df[["pclass", "parch"]].nunique()

#6
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

#7
df[df["embarked"] == "C"].head()


import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

#8
df[df["embarked"] != "S"].head()

#9
df[(df["age"] < 30) & (df["sex"] == "female")].head()

#10
df[(df["age"] > 70) | (df["fare"] > 500)].head()

#11
df.isnull().sum()

#12
df.drop("who", axis=1, inplace=True)

#13
df["deck"].mode()
type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

#14

type(df["age"].median())
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()

#15

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})  #önemli

