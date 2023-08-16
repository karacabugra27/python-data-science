x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning","Data Science")
s = {"Python", "Machine Learning", "Data Science" }

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))


lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

len(lst) #adım1

lst[0]  #adım2
lst[10]

data_list = lst[0:4] #adım3


lst.pop(8) #adım4

lst.append(44) #adım5

lst.insert(8,"N") #adım6



dict = {"Christian ": ["America", 18],
        "Daisy" : ["England", 12],
        "Antonio" : ["Spain", 22],
        "Dante" : ["Italy", 25]}

dict.keys()
dict.values()
dict.update({"Daisy":["England",13]})
dict.update({"Ahmet": ["Türkiye",24]})
dict.pop("Antonio")


l = [2,13,18,93,22]

def ayir(dizi):

    a=[]
    b=[]

    for index,eleman in enumerate(dizi):
        if index % 2 == 0:
            a.append(eleman)

        else:
            b.append(eleman)

     return (a,b)

ayir(l)


ogrenciler = ["ali", "veli", "ayşe", "talat", "zeynep", "ece"]
muhendis = []
tip = []

for i, ogrenci in enumerate(ogrenciler):
    if i < 3 :
        muhendis.append(ogrenci)

    else:
        tip.append(ogrenci)

for i, ogrenci in enumerate(ogrenciler,1):
    if i < 4 :
        print("mühendislik fakültesi ",i, "öğrenci:",ogrenci)

    else:
        print("tip fakültesi ", i, "öğrenci:", ogrenci)


ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu,kredi,kontenjan))

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def fonk(kume1,kume2):
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

fonk(kume1,kume2)









