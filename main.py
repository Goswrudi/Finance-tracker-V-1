import webbrowser
from datetime import datetime

def information():
    print('Welcome to Fintraa !')
    name = input('Enter your name : ')
    print(f'''\nHey {name}, Welcome to Fintraa !!  
The Job Eater of Accountants and Personal Assistants !!\n''')    
    return name # Returning name so the app can remember it

def show_settings():
    print('''Google Web-Softwares keys are:
S  -> Google Sheets 
D  -> Google Docs
P  -> Google PPT
C  -> Google Calendar               
GW -> Google Workspace''')

    print('\n' + '='*30 + '\n')    

    print('''Microsoft Web-Softwares keys are:
E  -> Microsoft Excel 
W  -> Microsoft Word 
P_MS -> Microsoft Powerpoint
MO -> Microsoft One 365''')
    print('='*30 + '\n')


class googlefuncs:
    # @staticmethod tells Python these functions don't need 'self'
    @staticmethod
    def O_sheets():
        webbrowser.open('https://sheets.google.com')

    @staticmethod
    def O_docs():
        webbrowser.open('https://docs.google.com')

    @staticmethod
    def O_ppt():
        webbrowser.open('https://docs.google.com/presentation/u/0/')

    @staticmethod
    def O_cal():
        webbrowser.open('https://calendar.google.com/')


class microsoftfuncs:
    @staticmethod
    def O_excel():
        webbrowser.open('https://excel.cloud.microsoft/en-gb/')

    @staticmethod
    def O_word():
        webbrowser.open('https://word.cloud.microsoft/en-gb/')

    @staticmethod
    def O_powerpoint():
        webbrowser.open('https://powerpoint.cloud.microsoft/en-gb/')

    @staticmethod
    def O_MO():
        webbrowser.open('https://www.microsoft.com/en-in/microsoft-365')


# # --- Main logic ---
# username = information()
# show_settings()

# # Capture input and immediately force it to uppercase using ()
# user_choice = input("Mention Today's Agenda (Enter Key): ").upper()

# # Handle choice logic
# if user_choice == 'S':
#     print("Opening Google Sheets...")
#     googlefuncs.O_sheets() # Fixed to call Sheets!

# elif user_choice == 'C':
#     print("Opening Google Calendar...")
#     googlefuncs.O_cal()

# elif user_choice == 'NONE':
#     print(f'\nNo problem, {username}... Fintraa is ready for anything you want!!')

# else:
#     print("\nInvalid key! Fintraa automation terminated.")