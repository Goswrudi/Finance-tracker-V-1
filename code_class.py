
import webbrowser
def information():
    # Brand Color Palette (Based on Logo)
    DEEP_BLUE = '\033[34m'   # Matching the large prominent 'F'
    LIGHT_BLUE = '\033[94m'  # Matching 'iinntra' text
    CYAN = '\033[36m'        # Accent headers
    BOLD = '\033[1m'
    RESET = '\033[0m'

    # Set a fixed mathematical width for the internal box content
    BOX_WIDTH = 48

    # Helper function to print a perfectly bounded text line
    def print_line(text, color=RESET):
        # Strip ANSI codes if any exist to calculate pure text length
        visible_len = len(text.replace(DEEP_BLUE, "").replace(LIGHT_BLUE, "").replace(CYAN, "").replace(BOLD, "").replace(RESET, ""))
        padding = BOX_WIDTH - visible_len
        print(f"{DEEP_BLUE}┃{RESET}  {color}{text}{RESET}{' ' * padding}{DEEP_BLUE}┃{RESET}")

    # 1. Top border frame closing
    print(f"{DEEP_BLUE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
    
    # 2. Centered Welcome Header
    welcome_text = f"{BOLD}{CYAN}W E L C O M E   T O{RESET}"
    # Dynamic spacing adjustment for the header line
    print_line(f"              {welcome_text}")
    print_line("") # Empty separator line
    
    # 3. Dynamic Logo Text mapping
    print_line(f"█▀▀ █ █ █▄ █ █▄ █ ▀█▀ █▀█ ▄▀█  {LIGHT_BLUE}▄▀█{RESET}", DEEP_BLUE)
    print_line(f"█▀  █ █ █ ▀█ █ ▀█  █  █▀▄ █▀█  {LIGHT_BLUE}█▀█{RESET}", DEEP_BLUE)
    print_line(f"▀   ▀ ▀ ▀  ▀ ▀  ▀  ▀  ▀ ▀ ▀ ▀  {LIGHT_BLUE}▀ ▀{RESET}", DEEP_BLUE)
    
    # 4. Bottom border frame closing
    print(f"{DEEP_BLUE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}\n")
    
    # 5. Interactive user login action
    name = input(f"{LIGHT_BLUE}➔{RESET} {BOLD}Enter your name:{RESET} ")
    
    # 6. Clean, professional brand greeting banner
    print("\n" + f"{LIGHT_BLUE}━{RESET}" * 60)
    print(f"  {DEEP_BLUE}❖{RESET} {BOLD}Hey {name}, Welcome to Fiinntra !!{RESET}")
    print(f"    {LIGHT_BLUE}The Job Eater of Accountants and Personal Assistants !!{RESET}")
    print(f"{LIGHT_BLUE}━{RESET}" * 60 + "\n")
    
    return name
    

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

