
##KOŞULLAR
def check(number):
    if (number == 10):
        print("sayi 10 a esit")

    elif(number < 10):
        print("sayi 10 dan küçük.")

    else:
        print("sayi 10'a esit degil.")


check(7)


##DÖNGÜLER

salaries = [1000, 2000, 5000, 15000]

def calculate_salary(salary, rate):
    return (salary*rate/100)+salary

for salary in salaries:

    if(salary<2500):
        print(calculate_salary(salary, 25))


    else:
        print(calculate_salary(salary, 15))


##MÜLAKAT SORUSU

range(len("bugra"))

for i in range(len("bugra")):
    print(i)

def fonk(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0  :
            new_string += string[string_index].upper()

        else:
            new_string += string[string_index].lower()

    print(new_string)

fonk("bugra")


## break, continue, while

maaslar = [1000, 2000, 3000, 5000]

for maas in maaslar:
    if maas == 3000:
        break
    print(maas)

for maas in maaslar:
    if maas == 2000:
        continue
    print(maas)

number = 5

while number <= 10:
    print(number)
    number += 1

## ENUMERATE OTOMATİK COUNTER/INDEXER ILE LOOP

A = []
B = []

students = ["ali", "veli", "mehmet", "cabbar"]


for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A)
print(B)


def alternating(string):
    new_string = ""

    for i , letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    print(new_string)

alternating("bugra baba nerede gelsin söyle")


## ZIP

a = ["bugra", "ali", "veli"]
b = [ 21, 25, 48]
c = ["maths", "software engineering", "scientist"]

print(list(zip(a,b,c)))

print(list(map(lambda x: x*20/100 + x, salaries)))








