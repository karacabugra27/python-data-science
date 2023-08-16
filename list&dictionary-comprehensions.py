#bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() for col in df.columns]

#isminde "ins" olanların başına flag olmayanların başına no_flag ekle

df.columns = ["FLAG" + col if "INS" in col else "NO_FLAG" + col for col in df.columns]


#keyi string value liste sözlük
# sadece sayısal değişkenler için

#uzun yol (python yerel yollarıyla)

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz ={}
agg_list = ["mean", "min", "max", "var"]

for col in df.columns:
    soz[col] = agg_list

#kısa yol


new_dict = {col : agg_list for col in df.columns}

df.head()
df[num_cols].head()

df[num_cols].agg(new_dict)
