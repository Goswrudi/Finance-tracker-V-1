
import webbrowser
import time

def open_sheet():
    sheet_url = 'https://sheets.google.com'
    print(f'Openning sheet .....')
    webbrowser.open(sheet_url)


name = input('''Hey , What's your name? :''')
print(f'Welcome {name} This side your personal finance bro: ')
print('')

choice1 = input('''What's your agenda today?.... press enter to continue ''')
sheet_choice = input('''Press 'S' to open Google Sheets ''')

# choice = input('''What's your agenda today? ''')

if(sheet_choice ==  'S'):
    open_sheet()

else:
    print('Something went wrong !')


