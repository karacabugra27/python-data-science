import seaborn as sns
import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", 5)
pd.set_option("display.width", 300)

df = sns.load_dataset("car_crashes")

##########################################
############ SORU 1 ######################
##########################################

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


##########################################
############ SORU 2 ######################
##########################################
df = sns.load_dataset("car_crashes")

[col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
##########################################
############ SORU 3 ######################
##########################################

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]

##########################################
######### PANDAS ALIŞTIRMALAR ############
##########################################

##########################################
############### SORU 1 ###################
##########################################

df = sns.load_dataset("titanic")
df.info
df.shape

##########################################
############### SORU 2 ###################
##########################################

df["sex"].value_counts()

##########################################
############### SORU 3 ###################
##########################################

df.nunique()

##########################################
############### SORU 4 ###################
##########################################

df["pclass"].unique()

##########################################
############### SORU 5 ###################
##########################################

df[["pclass","parch"]].nunique()

##########################################
############### SORU 6 ###################
##########################################

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype

##########################################
############### SORU 7 ###################
##########################################

df[df["embarked"] == "C"].head()

##########################################
############### SORU 8 ###################
##########################################

df[df["embarked"] != "S"].head()

##########################################
############### SORU 9 ###################
##########################################

df[(df["age"] <30 ) & (df["sex"] == "female")].head()

##########################################
############### SORU 10 ##################
##########################################

df[(df["fare"] > 500 ) | (df["age"] > 70)].head()

##########################################
############### SORU 11 ##################
##########################################

df.isnull().sum()

##########################################
############### SORU 12 ##################
##########################################

df.drop("who", axis=1, inplace= True)

##########################################
############### SORU 13 ##################
##########################################
#mode()[0] ifadesi hangi modu seçeceğimizi gösteriyor yani en çok tekrar eden 1. eleman demektir.
type(df["deck"].mode())
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

##########################################
############### SORU 14 ##################
##########################################

type(df["age"].median())
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()

##########################################
############### SORU 15 ##################
##########################################

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]}).head()

##########################################
############### SORU 16 ##################
##########################################

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda age : age_30(age))
df.head()

##########################################
############### SORU 17 ##################
##########################################

df = sns.load_dataset("tips")
df["time"].value_counts()
df.head()

##########################################
############### SORU 18 ##################
##########################################

df.groupby("time").agg({"total_bill" : ["sum", "min", "max", "mean"]})

##########################################
############### SORU 19 ##################
##########################################

df.groupby(["time", "day"]).agg({"total_bill" : ["sum", "min", "max", "mean"]})

##########################################
############### SORU 20 ##################
##########################################

#Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day").agg({"total_bill" : ["sum", "min", "max", "mean"],
                                                                          "tip" : ["sum", "min", "max", "mean"]})

##########################################
############### SORU 21 ##################
##########################################
#tekrar et

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), ["total_bill"]].mean()

#loc daha iyi öğren
##########################################
############### SORU 22 ##################
##########################################

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

##########################################
############### SORU 23 ##################
##########################################

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[0:30]
new_df.head()
