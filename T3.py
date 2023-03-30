
# Create a list of 10 elements of four different data types like int, string, complex and float.
user_list = [5, "hello", 4 + 3j, 6.5, 7, "world", 6 + 8j, 7.5, 9, "Welcome"];
print(user_list)

# Create a list of size 5 and execute the slicing structure
slice_list = [5, "hello", 4 + 3j, 6.5, 7]
print(slice_list[2:4])

# Write a program to get the sum and multiply of all the items in a given list.
def prod(mul):
    result = 1
    for i in mul:
        result = i * result
    return result


sum_product = [2,6,12,5,10]
print(prod(sum_product))
print(sum(sum_product));


# Find the largest and smallest number from a given list.
small_large_list = [15,55,22,25,28];
print(min(small_large_list))
print(max(small_large_list))

# Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = [num for num in numbers if num % 2 != 0]

print(new_numbers)
first_five = [num**2 for num in range(1, 6)]
last_five = [num**2 for num in range(26, 31)]

combined = first_five + last_five
print(combined)

# Write a program to replace the last element in a list with another list.
first_list = [1,3,5,7,9,10]
second_list = [2,4,6,8]
first_list.pop() 
print(first_list)
combined_list =  first_list+ second_list

print(combined_list)

# Create a new dictionary by concatenating the following two dictionaries:

a = {1:10, 2:20}
b = {3:30, 4:40}
c = a.copy()
c.update(b)
print(c)

# Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).

n = 5
squares_dict = {x: x*x for x in range(1, n+1)}

print(squares_dict)


# Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.

input_str = input("Enter comma-separated numbers: ")

num_list = input_str.split(',')

str_list = [str(num) for num in num_list]

str_tuple = tuple(str_list)

print("List of numbers as strings: ", str_list)
print("Tuple of numbers as strings: ", str_tuple)