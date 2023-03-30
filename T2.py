
# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.

number = int(input("enter the number"))
if(number % 3 == 0):
    print("Consultadd")
elif(number % 5 == 0):
    print("Python Training")
elif(number % 3 == 0 & number % 5 == 0):
    print("Consultadd- Python Training")
else:
    print("Number is not divisible by 3 and 5")

# Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.
option = int(input("Enter 1-addition, Enter 2-Subtraction, Enter 3-Division,Enter 4-Multiplication,Enter 5- Average"))
if(option != 5):
    num1 = int(input("enter the 1st number"))
    num2 = int(input("enter the 2nd number"))
if(option == 1):
    sum = num1 + num2
    print(sum)
elif(option == 2):
    sub = num1 - num2
    print(sub)
elif(option == 3):
    div = num1/num2
    print(div)
elif(option == 4):
    product = num1*num2
    print(product)
elif(option == 5):
    number1 = int(input("enter the 1st number"))
    number2 = int(input("enter the 2nd number"))
    avg= (number1 + number2)/2
    print(avg)
else:
    print("choose from the option")


# Flowchart
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))

avg = (a + b + c)/3
print("avg =", avg)

if(avg > a and avg > b and avg > c):
    print("avg is higher than a,b,c")
elif(avg > a and avg > b):
    print("avg is higher than a,b,c")
elif(avg > a and avg > c):
    print("avg is higher than a,c")
elif(avg > b and avg > c):
    print("avg is higher than b,c")
elif(avg > a):
    print("avg is just greather than a")
elif(avg > b):
    print("avg is just greather than b")
elif(avg > c):
    print("avg is just greather than c")

# Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("It's Over")
        break
    
    print("Good Going")
    continue

# write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.
result = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)
print(result)

# Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for i in range(7):
    if i == 3 or i == 6:
        continue  
    print(i, end=" ")

# Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

string_input = input("Enter a string: ")
digit_count = 0
letter_count = 0

for char in string_input:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print("Letters", letter_count, "Digits", digit_count)

# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

lucky_number = 42
answer = 'yes'

while answer == 'yes':
    guess = int(input("Guess the lucky number: "))
    if guess == lucky_number:
        print("Congratulations! You guessed the lucky number!")
        break  
    answer = input("Sorry, that's not it. Do you want to guess again? (yes/no) ")
    
print("Thanks for playing!")

# Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.

lucky_number = 42
counter = 1
while counter <= 5:
    guess = int(input("Type in the {} number: ".format(counter)))
    if guess == lucky_number:
        print("Good guess!")
        break  
    
    print("Try again!")
    
    counter += 1
    
print("Game over!")


# In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.


lucky_number = 42
counter = 1

while counter <= 5:
    guess = int(input("Type in the {} number: ".format(counter)))
    
    if guess == lucky_number:
        print("Good guess!")
        break  
    print("Try again!")
    counter += 1

if counter > 5:
    print("Sorry but that was not very successful")





