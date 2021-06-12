"""
source for excercises:
https://w3resource.com/python-exercises/modules/index.php
"""
import os
import random
import string
import datetime
import types
import decimal

# Module - random
# 1. Write a Python program to generate a random alphabetical string,
# random value between two integers (inclusive)
# and a random multiple of 7 between 0 and 70. Use random.randint()

x = ''
for i in range(0, 10):
    x += random.choice(string.ascii_letters)
print(x)

# two random int
print(random.randint(1, 10), random.randint(1, 10), sep=", ")

# random multiple of 7 between 0 and 70
print(random.randint(0, 10) * 7)

# 2. Write a Python program to select a random element from a list, set,
# dictionary (value) and a file from a directory. Use random.choice()
list_1 = ['a', 'b', 'c', 'd', 'e']
set_1 = {'f', 'g', 'h', 'i', 'j'}
dict_1 = {'k': 1, 'l': 2, 'm': 3, 'n': 4, 'o': 5}

print(random.choice(list_1))
print(random.choice(list(set_1)))
print(random.choice(list(dict_1.values())))
print(random.choice(os.listdir("C:\\")))

# 3. Write a Python program to generate a random alphabetical character,
# alphabetical string and alphabetical string of a fixed length.
# Use random.choice()
print(random.choice(string.ascii_letters))
print(''.join([random.choice(string.ascii_letters) for x in range(10)]))
print(''.join([random.choice(string.ascii_letters) for x in
               range(random.randint(0, 10))]))

# 4. Write a Python program to construct a seeded random number generator,
# also generate a float between 0 and 1, excluding 1. Use random.random()

print(random.Random().random())
print(random.random())

# 5. Write a Python program to generate a random integer between 0 and 6 -
# excluding 6, random integer between 5 and 10 - excluding 10, random integer
# between 0 and 10, with a step of 3 and random date between two dates.
# Use random.randrange()

print(random.randrange(5))
print(random.randrange(5, 10))
print(random.randrange(0, 10, 3))
date1 = datetime.date(2021, 1, 1)
date2 = datetime.date.today()
delta = (date2 - date1).days
print((date1 + datetime.timedelta(days=random.randrange(delta + 1))))

# 6. Write a Python program to shuffle the elements of a given list.
# Use random.shuffle()
random.shuffle(list_1)
print(list_1)
# 7. Write a Python program to generate a float between 0 and 1,
# inclusive and generate a random float within a specific range.
# Use random.uniform()
print(random.uniform(0, 1))
print(random.uniform(2.0, 5.0))
# 8. Write a Python program to create a list of random integers and randomly
# select multiple items from the said list. Use random.sample()
list_2 = list([random.randint(0, 100) for i in range(20)])
print(random.sample(list_2, random.randint(0, 20)))
# 9. Write a Python program to set a random seed and get a random number between
# 0 and 1. Use random.random.
random.seed(0)
print(random.random())
random.seed(1)
print(random.random())


# Module - types
# 1. Write a Python program to check if a function is a user-defined function
# or not. Use types.FunctionType, types.LambdaType()
def new_fct():
    return 1


print(isinstance(new_fct, types.FunctionType))
print(isinstance(new_fct, types.LambdaType))
print(isinstance(sum, types.FunctionType))
print(isinstance(sum, types.LambdaType))


# 2. Write a Python program to check if a given value is a method of a
# user-defined class. Use types.MethodType()
class S:
    def a():
        return 1


print(isinstance(new_fct, types.MethodType))
print(isinstance(sum, types.MethodType))
print(isinstance(S().a, types.MethodType))


# 3. Write a Python program to check if a given function is a generator or not.
# Use types.GeneratorType()
def gen(x):
    yield x


print(isinstance(new_fct, types.GeneratorType))
print(isinstance(sum, types.GeneratorType))
print(isinstance(S().a, types.GeneratorType))
print(isinstance(gen(1), types.GeneratorType))
# 4. Write a Python program to check if a given value is compiled code or not.
# Also check if a given value is a module or not.
# Use types.CodeType, types.ModuleType()
# given_value = compile(new_fct())
# print(isinstance(given_value, types.CodeType))
# print(isinstance(given_value, types.ModuleType))
print(isinstance(new_fct, types.CodeType))
print(isinstance(sum, types.CodeType))
print(isinstance(S().a, types.CodeType))
print(isinstance(gen(1), types.CodeType))

