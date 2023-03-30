# Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
import sys

while True:
    try:
        file_name = sys.argv[1]
        file = open(file_name, 'r')
        break
    except (IndexError, FileNotFoundError):
        print("Oops! File not found. Please enter a valid file name:")
        file_name = input()
file_content = file.read()
print(file_content)

file.close()

# Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
while True:
    try:
        num = input("Enter a four-digit number: ")
        if len(num) != 4:
            raise Exception("The length is too short/long !!! Please provide only four digits")
        print("You entered:", num)
        break
    except Exception as e:
        print("Oops!", e)

# Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

correct_username = "myuser"
correct_password = "mypassword"

max_attempts = 3

for attempt in range(max_attempts):
    username = input("Enter username: ")
    password = input("Enter password: ")
    retype_password = input("Re-type password: ")

    if username == correct_username and password == correct_password and password == retype_password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password!")
        if attempt == max_attempts - 1:
            print("Sorry, you have exceeded the maximum number of attempts.")
        else:
            print("Please try again.")

# Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.
with open("doc.txt", "r") as file:
    contents = file.read()

    words = contents.split()

    even_words = filter(lambda word: len(word) % 2 == 0, words)

    result = " ".join(even_words)

    print(result)
