# Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.

string = "Hello World"

uppercase_chars = [char for char in string if char.isupper()]

print(uppercase_chars)

# Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also

students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "History"]

pairs = zip(students, subjects)

dictionary = {}
for pair in pairs:
    dictionary[pair[0]] = pair[1]

print(dictionary)

dictionary = {students[i]: subjects[i] for i in range(len(students))}

print(dictionary)

# Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
def reverse_string(string):
    for i in range(len(string)-1, -1, -1):
        yield string[i]

input_string = "Consultadd Training"

reversed_string = "".join(reverse_string(input_string))

print(reversed_string)

# Write an example on decorators.
def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Hello, " + result
    return wrapper

@greeting_decorator
def greet(name):
    return name

print(greet("John"))