##LIST COMPREHENSIONS

salaries = [1000, 2000, 3000, 5000]

[salary*20/100 + salary if salary < 2500 else salary*10/100 + salary for salary in salaries]

 ##DICT COMPREHENSIONS

dictionary = {"a":2,
     "b":3,
     "c":4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k.upper() : v ** 2 for (k,v) in dictionary.items()}

numbers = range(10)

{n : n ** 2 for n in numbers if n % 2 == 0 }









