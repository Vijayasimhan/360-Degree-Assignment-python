# Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
a, b , c = 1, [2, 3, 4], 'string'
print(type(a))
print(type(b))
print(type(c))

# Create a variable of type complex and swap it with another variable of type integer.
a = 4 + 5j
b = 5
temp = a
a = b
b = temp
print(a)
print(b)

# Swap two numbers using a third variable and do the same task without using any third variable.
a = 10
b = 5
(a,b) = (b,a)
print(a,b)

a = 107
b = 25
c = a + b
b = c - b
a = c - a
print(a,b)

# Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.
# py2
# user_input = raw_input("Enter some text: ")
# print "You entered:", user_input

# py3
user_imput = input("Hello Everyone!")
print(user_imput)

# Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.
num1 = int(input("Enter any number between 1 and 10"))
num2 = int(input("enter another number between 1 and 10"))
z = num1+num2
final = z + 30
print(final)


# Write a program to check the data type of the entered values.
value = input("Enter a value:")
if isinstance(value, int):
  print("The data type of the input value is: int")
elif isinstance(value, float):
  print("The data type of the input value is: float")
elif isinstance(value, str):
  print("The data type of the input value is: string")
else:
  print("The data type of the input value is: unknown")


# Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
UpperCamelCase = "hello"
lowerCamelCase = "world"
snake_case = "!"
UPPERCASE = "HELLO"
print(UpperCamelCase, lowerCamelCase, snake_case, UPPERCASE)

# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?

# Answer
# Yes, if you assign a different data type value to a variable, it will change the value of the variable. 
# This is because variables are used to store values, and when you assign a new value to a variable,
# the old value is replaced with the new one.
# a = 10. a is an integer with a value of 10
# a = hello. a is now a string with a value of hello;