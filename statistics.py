# Create some functios methods and functions which will help fintraa for the statistics overview 

# Creating Statistics calculator 

import numpy as np

def user_data():
    data = input("Enter data separated by commas: ")

    data = data.split(",")

    data = [float(x) for x in data]

    print(data)

user_data()
