# Create some functios methods and functions which will help fintraa for the statistics overview 

# Creating Statistics calculator 

import numpy as np

class user_data():

     def __init__(self):

        data = input("Enter data separated by commas: ")

        data = data.split(",")

        self.user_final_data = [float(x) for x in data]

user = user_data()

def Median():
        print(f'The Median of the following data {user.user_final_data} is : ({np.median(user.user_final_data)})')
        # Median function

def Maximum():
        print(f'The Maximum of the following data {user.user_final_data} is : ({np.max(user.user_final_data)})')
        # Maximum

# print(f'The Minimum of the following data {user.user_final_data} is : ({np.minimum(user.user_final_data)})')
# minimum

# print(f'The range of the following data {user.user_final_data} is : ({np.arange(user.user_final_data)})')
# range

def Sum():
        print(f'The sum of the following data {user.user_final_data} is : ({np.sum(user.user_final_data)})')
        # Sum

def Avg():
        print(f'The average of the followig data {user.user_final_data} is : ({np.average(user.user_final_data)})') 
        #average

def Variance():
        print(f'The Variance of the following data {user.user_final_data} is : ({np.var(user.user_final_data)})')
        #Variance 

def Standard_deviation():
        print(f'The Median of the following data {user.user_final_data} is : ({np.std(user.user_final_data)})')
        # Standard deviation 

def percantile():
        import numpy as np

def percentile():  # Fixed typo in function name
    # Added the required '50' for the median calculation
    median_val = np.percentile(user.user_final_data, 50)
    print(f'The Median of the following data {user.user_final_data} is : ({median_val})')
 

# Creating the seprtae functions cause it will make easier to call

