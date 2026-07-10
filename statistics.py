# Create some functios methods and functions which will help fintraa for the statistics overview 

# Creating Statistics calculator 

import numpy as np

class user_data():

     def __init__(self):

        data = input("Enter data separated by commas: ")

        data = data.split(",")

        self.user_final_data = [float(x) for x in data]

user = user_data()

print(f'The average of the followig data {user.user_final_data} is : ({np.average(user.user_final_data)})') 
