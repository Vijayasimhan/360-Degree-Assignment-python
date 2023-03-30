# Write a program to reverse a string.
def reverse_string(user_input):
    reversed_string = user_input[::-1]
    return reversed_string

user_input = input("Enter the string")
print(reverse_string(user_input))

# # Write a function that accepts a string and prints the number of uppercase letters and lowercase
# # letters.
def case_count(value):
    num_upper = 0
    num_lower = 0
    for char in value:
        if char.isupper():
            num_upper += 1
        elif char.islower():
            num_lower += 1
    print("Number of uppercase letters:", num_upper)
    print("Number of lowercase letters:", num_lower)

user_value = input("Enter the string")
case_count(user_value)

# # Create a function that takes a list and returns a new list with unique elements of the first list.
def get_unique_elements(lst):
    return list(set(lst))

first_list = [2,3,4,5,6,5]
unique_list = get_unique_elements(first_list)
print(unique_list) 

# # Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# # in a hyphen-separated sequence after sorting them alphabetically.
input_str = input("Enter a hyphen-separated sequence of words: ")

words_list = input_str.split("-")

words_list.sort()

sorted_str = "-".join(words_list)

print(sorted_str)

# # Write a program that accepts a sequence of lines as input and prints the lines after making all
# # characters in the sentence capitalized.
input_str = input("Enter a the words: ") 
x = input_str.upper()
print(x)
# # Define a function that can receive two integral numbers in string form and compute their sum and
# # print it in the console.
def add_numbers(num1, num2):
    sum = int(num1) + int(num2)
    print("The sum of", num1, "and", num2, "is", sum)

num1 = "10"
num2 = "20"
add_numbers(num1, num2)

# # Define a function that can accept two strings as input and print the string with the maximum length
# # in the console. If two strings have the same length, then the function should print both the strings line
# # by line.
def add_numbers(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)

str1 = "100"
str2 = "20"
add_numbers(str1, str2)

# # Define a function which can generate and print a tuple where the values are square of numbers
# # between 1 and 20 (both 1 and 20 included).
def generate_square_tuple():
    square_tuple = ()

    for i in range(1, 21):
        square_tuple += (i ** 2,)

    print(square_tuple)

generate_square_tuple()

# Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
def showNumbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

showNumbers(10)

# Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print(even_numbers)

# Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
given_list = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, given_list))
squares = map(lambda x: x ** 2, even_numbers) 
print(list(squares))

# Write a function to compute 5/0 and use try/except to catch the exceptions
def numbers(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Result is:", result)

a = 5
b = 0
numbers(a,b)
# Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce

concatenate = lambda x, y: str(x) + str(y)
numbers = [1, 2, 3, 4, 5, 6, 7]
result = reduce(concatenate, numbers)
result = int(result) 
print(result) 


# Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

numbers = range(1, 101)

result = filter(lambda x: x % 3 != 0 and x % 7 == 0, numbers)
result = list(result)

print(result) 

# Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
result = list(result)
print(result)  

# 16
# 2
# This is because the foo() function contains a try statement that attempts to return the value 1, but immediately afterwards, a finally statement returns the value 2. 
# The finally block is executed regardless of whether the try block raises an exception or not, so the value 2 will always be returned.
# When the foo() function is called and its return value is assigned to the variable k, the value 2 is returned and assigned to k. 
# When k is printed to the console, the value 2 is printed.

# The code you provided will result in a NameError because the function f is not defined.
# Assuming the function f is defined somewhere else in the program, the code will execute the try block and attempt to call the function f with the arguments x and 4. 
# If this call raises an exception, the finally block will execute and print the strings 'after f' and 'after f?' to the console.
# If the call to f does not raise an exception, the finally block will still execute, but the program will continue executing after the finally block instead of immediately exiting due to an unhandled exception.

