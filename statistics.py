# Create some functios methods and functions which will help fintraa for the statistics overview 

# Creating Statistics calculator 

import numpy as np

class user_data():
    
    data = input("Enter data separated by commas: ")

    data = data.split(",")

    data = [float(x) for x in data]

    final_user_data = data
    print(final_user_data)

user_data()

print(np.average(user_data.final_user_data))
