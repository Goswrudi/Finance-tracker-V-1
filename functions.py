# The purpose of creating this file is to maks sure not everything dfirectly writtend in main file
# 

import webbrowser

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


class microsoftfuncs:

    def O_excel():
        excel_url = 'https://excel.cloud.microsoft/en-gb/'
        open = webbrowser.open(excel_url)

    def O_word():
        word_url = 'https://word.cloud.microsoft/en-gb/'
        open = webbrowser.open(word_url)

    def O_powerpoint():
        pptx_url = 'https://powerpoint.cloud.microsoft/en-gb/'
        open = webbrowser.open(pptx_url)

        
    def O_MO():
        MO_url = 'https://www.microsoft.com/en-in/microsoft-365'
        open = webbrowser.open(MO_url)
 
