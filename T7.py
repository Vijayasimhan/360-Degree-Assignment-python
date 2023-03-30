# Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.
import math

C = 50
H = 30

D = input("Enter the values of D (comma-separated sequence): ")

D_list = D.split(",")

for d in D_list:
    d = int(d)
    Q = math.sqrt((2 * C * d) / H)
    print("Q =", Q)

# Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length * self.length
    
square = Square(5)
print("Area of square:", square.area())

# Create a class to find three elements that sum to zero from a set of n real numbers
class ThreeSum:
    def __init__(self, arr):
        self.arr = arr
    
    def findTriplets(self):
        n = len(self.arr)
        found = False
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.arr[i] + self.arr[j] + self.arr[k] == 0:
                        print("Triplets found:", self.arr[i], self.arr[j], self.arr[k])
                        found = True
        if not found:
            print("No triplets found.")
arr = [1, -2, 3, -4, 5, -6, 0]
three_sum = ThreeSum(arr)
three_sum.findTriplets()

# Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, t):
        minutes = self.minutes + t.minutes
        hours = self.hours + t.hours + (minutes // 60)
        minutes = minutes % 60
        return Time(hours, minutes)
    
    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")
    
    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minute")

t1 = Time(2, 50)
t2 = Time(1, 20)

t3 = t1.addTime(t2)
t3.displayTime()   
t3.displayMinute()   

# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.
class Person:
    def __init__(self, age):
        if age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = age
        
    def yearPasses(self, years):
        self.age += years
        
    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")
p = Person(25)
p.amIOld()         
p.yearPasses(5)
p.amIOld()        
p.yearPasses(-2)
p.amIOld()        
p = Person(10)
p.amIOld()      
p.yearPasses(5)
p.amIOld()       