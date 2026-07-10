# Create some functios methods and functions which will help fintraa for the statistics overview 

import numpy as np


numbers = input('Enter a number : ') 
print(numbers)


# convert the numbers from string to list
numbers = input("Enter numbers separated by commas: ")

numbers = numbers.split(",")

numbers = [float(x) for x in numbers]

print(numbers)