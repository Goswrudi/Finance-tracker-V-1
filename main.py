import webbrowser
from datetime import datetime
from code_class import information
from code_class import show_settings
from code_class import googlefuncs
from code_class import microsoftfuncs
from calc import FinancialData
from calc import StatisticsCalculator


###      --- Main logic ---     ###
print('===============================')
print('')

username = information()

print('===============================')
print('')

# show_settings()

### Creating seprate logic ###

print('===============================')
print('')

print('Q for MS/Google plugins')
print('C for Calculator:') 
print('S for Setting:')       

print('')
print('===============================')


Main_choice = input('''Today's Agenda? : ''').upper()

def logic_choice():
    if Main_choice == 'Q':
        None

    elif Main_choice == 'C':
        print("Starting Calculator Application...")
        
        # 1. Initialize the financial data prompt
        session_data = FinancialData()
        
        # 2. Pass the cleaned data to the calculator
        fintraa_calc = StatisticsCalculator(session_data.clean_data)
        
        # 3. Display the report
        fintraa_calc.display_all_stats()
        
    elif Main_choice == 'S':
        show_settings()

    else:
        print('Wrong choice entred by the user : ')

        
# --- Execution Guard ---
# Put this at the very bottom of your file to trigger your function!
if __name__ == "__main__":
    logic_choice()


# # Handle choice logic

# if user_choice == 'S':
#     print("Opening Google Sheets...")
#     googlefuncs.O_sheets() # Fixed to call Sheets!

# elif user_choice == 'D':
#     print("Opening Google Docs...")
#     googlefuncs.O_docs()

# elif user_choice == 'P':
#     print("Opening Google PPTX...")
#     googlefuncs.O_ppt()

# elif user_choice == 'C':
#     print("Opening Google Calendar...")
#     googlefuncs.O_cal()

# # elif user_choice == 'GW':
# #     print("Opening Google Workspace...")
# #     googlefuncs.O_docs()

# # Adding the microsoft functions 


# if(user_choice == 'E'):
#     print('Openning Micosoft excel')
#     microsoftfuncs.O_excel()

# elif(user_choice == 'W'):
#     print('Openning Micosoft Word')
#     microsoftfuncs.O_word()

# elif(user_choice == 'P_MS'):
#     print('Openning Micosoft Powewrpoint')
#     microsoftfuncs.O_powerpoint()

# elif(user_choice == 'MO'):
#     print('Openning Micosoft One 365')
#     microsoftfuncs.O_MO()

# else:
#      print("\nInvalid key! Fintraa automation terminated.")