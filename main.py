
# Information for the user

import webbrowser

def information():
    note = print('Welcome to the Fintraa !')
    name = input('Enter your name : ')
    greets = print(f'''Hey {name} , Welcome to Fintraa !!  
The Job Eater of Accountant and Personal Assitant !! ''') 
    
information()


def setting():
 
    G = print('''Google Web-Softwares key are ;
S for Google Sheets 
D for Google Docs
P for Google PPT
C for Google Calendor              
GW for Google workspace              ''')
    
    print('')
    
    M = print('''Micorosft Web-Softwares key are ;
e for Micorosft Excel 
w for Micorosft Word 
p for Microsoft Powerpoint
MO for Microsoft one               
              ''')


setting()



# 1 = input('To See all Settings/keybord shortcut press * ')

# if(1 == '*'):


def O_sheets():
    sheets_url = 'https://sheets.google.com'
    open = webbrowser.open(sheets_url)

def O_docs():
    docs_url = 'https://docs.google.com'
    open = webbrowser.open(docs_url)

def O_ppt():
    ppt_url = 'https://docs.google.com/presentation/u/0/'
    open = webbrowser.open(ppt_url)

def O_cal():
    cal_url = 'https://calendar.google.com/'
    open = webbrowser.open(O_cal)

    