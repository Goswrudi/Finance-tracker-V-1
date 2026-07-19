import webbrowser

def information():
    DEEP_BLUE, LIGHT_BLUE, CYAN, BOLD, RESET = '\033[34m', '\033[94m', '\033[36m', '\033[1m', '\033[0m'
    BOX_WIDTH = 48

    def print_line(text, color=RESET):
        visible_len = len(text.replace(DEEP_BLUE, "").replace(LIGHT_BLUE, "").replace(CYAN, "").replace(BOLD, "").replace(RESET, ""))
        padding = BOX_WIDTH - visible_len
        print(f"{DEEP_BLUE}┃{RESET}  {color}{text}{RESET}{' ' * padding}{DEEP_BLUE}┃{RESET}")

    print(f"{DEEP_BLUE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
    print_line(f"              {BOLD}{CYAN}W E L C O M E   T O{RESET}")
    print_line("")
    print_line(f"█▀▀ █ █ █▄ █ █▄ █ ▀█▀ █▀█ ▄▀█  {LIGHT_BLUE}▄▀█{RESET}", DEEP_BLUE)
    print_line(f"█▀  █ █ █ ▀█ █ ▀█  █  █▀▄ █▀█  {LIGHT_BLUE}█▀█{RESET}", DEEP_BLUE)
    print_line(f"▀   ▀ ▀ ▀  ▀ ▀  ▀  ▀  ▀ ▀ ▀ ▀  {LIGHT_BLUE}▀ ▀{RESET}", DEEP_BLUE)
    print(f"{DEEP_BLUE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}\n")
    
    name = input(f"{LIGHT_BLUE}➔{RESET} {BOLD}Enter your name:{RESET} ")
    print("\n" + f"{LIGHT_BLUE}━{RESET}" * 60)
    print(f"  {DEEP_BLUE}❖{RESET} {BOLD}Hey {name}, Welcome to Fiinntra !!{RESET}")
    print(f"    {LIGHT_BLUE}Not your avg 'Finance Tracker'💢 !!{RESET}")
    print(f"{LIGHT_BLUE}━{RESET}" * 60 + "\n")
    return name

def show_settings():
    print('''\nGoogle Web-Softwares keys are:
S  -> Google Sheets 
D  -> Google Docs
P  -> Google PPT
C  -> Google Calendar               
GW -> Google Workspace
\n==============================\n
Microsoft Web-Softwares keys are:
E  -> Microsoft Excel 
W  -> Microsoft Word 
P_MS -> Microsoft PowerPoint
MO -> Microsoft One 365''')
    print('='*30 + '\n')

def calc_setting():
    print('=======================================')
    print(''' Calculator Software keys are : 
S_C -> Statistics Calculator
A_C -> Arithmetic Calculator

  Arithmetic Sub-keys:
  A -> Addition
  B -> Subtraction            
  C -> Multiplication
  D -> Division''')
    print('=======================================')

class googlefuncs:
    @staticmethod
    def O_sheets(): webbrowser.open('https://sheets.google.com')
    @staticmethod
    def O_docs(): webbrowser.open('https://docs.google.com')
    @staticmethod
    def O_ppt(): webbrowser.open('https://docs.google.com/presentation/u/0/')
    @staticmethod
    def O_cal(): webbrowser.open('https://calendar.google.com/')

class microsoftfuncs:
    @staticmethod
    def O_excel(): webbrowser.open('https://excel.cloud.microsoft/en-gb/')
    @staticmethod
    def O_word(): webbrowser.open('https://word.cloud.microsoft/en-gb/')
    @staticmethod
    def O_powerpoint(): webbrowser.open('https://powerpoint.cloud.microsoft/en-gb/')
    @staticmethod
    def O_MO(): webbrowser.open('https://www.microsoft.com/en-in/microsoft-365')