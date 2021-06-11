"""
source for excercises:
https://www.w3resource.com/python-exercises/python-functions-exercises.php
"""


# 1. Write a Python function to find the Max of three numbers.
def max_of_three(a: int, b: int, c: int):
    return print(max(a, b, c))


# max_of_three(234,456,678)

# 2. Write a Python function to sum all the numbers in a list.
def sum_all_in_list(input_list: list):
    return print(sum(input_list))


# sum_all_in_list([1, 2345, 3423, 54])

# 3. Write a Python function to multiply all the numbers in a list.
def multiply_all_in_list(input_list: str):
    result = 1
    for element in input_list:
        result = result * element
    return print(result)


# multiply_all_in_list([1,10,10,])

# 4. Write a Python program to reverse a string.
def reverse_string(input_string: str):
    return print(input_string[::-1])


# reverse_string('reversed text sample')

# 5. Write a Python function to calculate the factorial of a number
# (a non-negative integer). The function accepts the number as an argument.
def factorial(x: int):
    if x > 1:
        return x * factorial(x - 1)
    return 1


# print(factorial(6))

# 6. Write a Python function to check whether a number is in a given range.
def number_in_range(x: int, rng):
    if x in range(rng[0], rng[1]):
        print(f'number {x} is in range {rng}')
    else:
        print(f'number {x} is out of range {rng}')


# number_in_range(12, (1, 6))

# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
def count_upper_and_lower(text: str):
    return print(f'upper case letters: '
                 f'{sum(1 for letter in text if letter.isupper())}',
                 f'lower case letters: '
                 f'{sum(1 for letter in text if letter.islower())}', sep='\n')


text_sample = 'sAMple OF tEXt ThAt Has rANdOmL UppEr aNd Low cASesE letteRs' \
              ' gENERaTeD ONlIne FoR pUrposE OF trAINiNg'


# count_upper_and_lower(text_sample)

# 8. Write a Python function that takes a list and returns a new list with
# unique elements of the first list.
def unique_elements_of_list(input_list: list):
    return print(f'unique elements of list: '
                 f'{", ".join([str(e) for e in set(input_list)])}')


# unique_elements_of_list(text_sample)

# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def prime_number(number: int):
    if number > 1:
        if number == 2:
            return print(f'{number} is prime')
        else:
            for i in range(2, number):
                if number % i == 0:
                    return print(f'{number} is not prime')
                else:
                    return print(f'{number} is prime')
    else:
        return print(f'{number} is not prime')


# prime_number(9)
# prime_number(2)
# prime_number(1)
# prime_number(6)
# prime_number(5)

# 10. Write a Python program to print the even numbers from a given list.
def even_numbers(input_list: list):
    return print(f'even numbers from given list:'
                 f' {", ".join([str(x) for x in input_list if x % 2 == 0])}')


random_list = [96, 3, 26, 76, 10, 43, 8, 32, 71, 89, 73, 61, 17, 100, 37, 94,
               58, 35, 93, 29, 46, 18, 86, 68, 90]


# even_numbers(random_list)

# 11. Write a Python function to check whether a number is perfect or not.
def perfect_number(number: int, total=0):
    for i in range(1, number):
        if number % i == 0:
            total = total + i
    if total == number:
        print(f'{number} is a Perfect Number')
    else:
        print(f'{number} is not a Perfect Number')


# perfect_number(28)
# perfect_number(2812)
# perfect_number(6)
# perfect_number(223)

# 12. Write a Python function that checks whether a passed string is palindrome
# or not.
def palindrome(text: str):
    if text == text[::-1]:
        print('given string is palindrome')
    else:
        print('given string is not palindrome')


# palindrome('aibohphobia')
# palindrome('text')
# palindrome('palindrome')
# palindrome('murdrum')

# 13. Write a Python function that prints out the first n rows of Pascal's
# triangle.
def first_rows_of_pascal(rows: int):
    row_1 = [1]
    print((str(row_1[0])).center(100))
    for x in range(rows - 1):
        nxt_row = [1]
        for y in range(len(row_1) - 1):
            nxt_row.append(row_1[y] + row_1[y + 1])
        nxt_row.append(1)
        row_1 = nxt_row
        print(' '.join([str(n) for n in nxt_row]).center(100))


# first_rows_of_pascal(10)

# 14. Write a Python function to check whether a string is a pangram or not.
# all letters
# https://vuyisile.com/python-how-to-generate-a-list-of-letters-in-the-alphabet/
def pangram(input_text: str):
    input_text = ''.join([i for i in input_text if i.isalpha()])
    converted_text = sorted(list(set(input_text.lower())))
    if converted_text == list(map(chr, range(97, 123))):
        print('given text is pangram')
    else:
        print('given text is not pangram')


pangram('A quick brown fox jumps over the lazy dog')
pangram('Just keep examining every low bid quoted for zinc etchings.')
pangram(text_sample)

# 15. Write a Python program that accepts a hyphen-separated sequence of words
# as input and prints the words in a hyphen-separated
# sequence after sorting them alphabetically.


# 16. Write a Python function to create and print a list where the values
# are square of numbers between 1 and 30 (both included).
# 17. Write a Python program to make a chain of function decorators
# (bold, italic, underline etc.) in Python.
# 18. Write a Python program to execute a string containing Python code.
# 19. Write a Python program to access a function inside a function.
# 20. Write a Python program to detect the number of local variables
# declared in a function.
