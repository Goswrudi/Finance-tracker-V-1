import webbrowser
from datetime import datetime

from code_class import information, show_settings, googlefuncs, microsoftfuncs , calc_setting , daily_reports , weekly_reports
from calc import FinancialData, StatisticsCalculator, Arthmetic
from reports import daily , weekly

def logic_choice(choice):
    # --- GOOGLE & MICROSOFT PLUGINS ---
    if choice == 'Q':
        show_settings() 
        plugin_choice = input("\nEnter plugin key (e.g., S, D, E, W): ").upper()
        
        # Google Handlers
        if plugin_choice == 'S':
            print("Opening Google Sheets...")
            googlefuncs.O_sheets()
        elif plugin_choice == 'D':
            print("Opening Google Docs...")
            googlefuncs.O_docs()
        elif plugin_choice == 'P':
            print("Opening Google Slides...")
            googlefuncs.O_ppt()
        elif plugin_choice == 'C':
            print("Opening Google Calendar...")
            googlefuncs.O_cal()
            
        # Microsoft Handlers
        elif plugin_choice == 'E':
            print("Opening Microsoft Excel...")
            microsoftfuncs.O_excel()
        elif plugin_choice == 'W':
            print("Opening Microsoft Word...")
            microsoftfuncs.O_word()
        elif plugin_choice == 'P_MS':
            print("Opening Microsoft PowerPoint...")
            microsoftfuncs.O_powerpoint()
        elif plugin_choice == 'MO':
            print("Opening Microsoft OneNote...")
            microsoftfuncs.O_MO()
        else:
            print(f"\n[{plugin_choice}] is an invalid plugin key! Returning to main.")



    # --- CALCULATOR ---
    elif choice == 'C':
        calc_setting()
        calc_type = input("\nchoose your calculator type A_C OR S_C ").upper()

        if(calc_type == 'A_C'):
            print('Opening Airthmetic calculator : ')
            op_choice = input("Select Operation (A=Add, B=Sub, C=Mul, D=Div): ").upper()
            if(op_choice == 'A'): Arthmetic.Addition()
            elif(op_choice == 'B'): Arthmetic.Subtraction()
            elif(op_choice == 'C'): Arthmetic.Multiplication()
            elif(op_choice == 'D'): Arthmetic.Divide()
            else: print('Something went worng , May user enterd something else')


        elif calc_type == 'S_C':
            try:
                session_data = FinancialData()
                if not session_data.clean_data:
                    print("Error: No valid data entered.")
                    return
                fintraa_calc = StatisticsCalculator(session_data.clean_data)
                fintraa_calc.display_all_stats()
            except ValueError:
                print("Error: Invalid input data format.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Unknown calculator system type selection.")

 # --- SETTINGS MAIN VIEW ---
    elif choice == 'S':
        show_settings()
    

    elif choice == 'R':
        print('Opening Report calculator : ')
        rc = input('Select Report operation (D=Daily report , W = Weekly report , M = Monthly report). ').upper()
        if(rc == 'D'): daily()
        elif(rc == 'W'): None
        elif(rc == 'M'): None
        else: print('Something went Wrong, May operation enterd by the user :( ')

    else:
        print(f"\nInvalid key [{choice}]! Fintraa execution aborted.")


def run_app():
    print('===============================')
    username = information()
    print('===============================')
    print('Q for MS/Google plugins')
    print('C for Calculator') 
    print('S for Settings')      
    print('R for Reports')
    print('===============================')
    
    main_choice = input('''Today's Agenda? : ''').upper()
    logic_choice(main_choice)

if __name__ == "__main__":
    run_app()
