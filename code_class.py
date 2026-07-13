# Setting function

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
