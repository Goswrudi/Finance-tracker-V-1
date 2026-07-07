
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


class googlefuncs:

    def O_sheets():
        sheets_url = 'https://sheets.google.com'
        webbrowser.open(sheets_url)

    def O_docs():
        docs_url = 'https://docs.google.com'
        webbrowser.open(docs_url)

<<<<<<< HEAD
    def O_ppt():
        ppt_url = 'https://docs.google.com/presentation/u/0/'
        webbrowser.open(ppt_url)

    def O_cal():
        cal_url = 'https://calendar.google.com/'
        webbrowser.open(cal_url)

# googlefuncs.O_cal()

# def O_excel():
#     excel_url = 'https://excel.cloud.microsoft/en-gb/'
#     open = webbrowser.open(excel_url)

# def O_word():
#     word_url = 'https://word.cloud.microsoft/en-gb/'
#     open = webbrowser.open(word_url)

# def O_powerpoint():
#     pptx_url = 'https://powerpoint.cloud.microsoft/en-gb/'
#     open = webbrowser.open(pptx_url)

=======
class googlefuncs:

    def O_sheets():
        sheets_url = 'https://sheets.google.com'
        webbrowser.open(sheets_url)

    def O_docs():
        docs_url = 'https://docs.google.com'
        webbrowser.open(docs_url)

    def O_ppt():
        ppt_url = 'https://docs.google.com/presentation/u/0/'
        webbrowser.open(ppt_url)

    def O_cal():
        cal_url = 'https://calendar.google.com/'
        webbrowser.open(cal_url)


# def O_excel():
#     excel_url = 'https://excel.cloud.microsoft/en-gb/'
#     open = webbrowser.open(excel_url)

# def O_word():
#     word_url = 'https://word.cloud.microsoft/en-gb/'
#     open = webbrowser.open(word_url)

# def O_powerpoint():
#     pptx_url = 'https://powerpoint.cloud.microsoft/en-gb/'
#     open = webbrowser.open(pptx_url)

>>>>>>> 8116867 (modifed the file)
# def O_MO():
#     MO_url = 'https://www.microsoft.com/en-in/microsoft-365'
#     open = webbrowser.open(MO_url)
 
