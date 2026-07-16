import webbrowser
from datetime import datetime

from code_class import information, show_settings, googlefuncs, microsoftfuncs , calc_setting
from calc import FinancialData, StatisticsCalculator, Arthmetic

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
            


        # try:
        #     data = Arthmetic()
        #     if not session_data.clean_data:
        #         print("Error: No valid data entered. Please enter numbers separated by commas.")
        #         return # Exits this function cleanly without crashing
                
        #     fintraa_calc = Arthmetic(data.clean_data)
        #     fintraa_calc.display_all_stats()
            
        # except ValueError:
        #     print("Error: Invalid input. Please only enter numbers (e.g., 100, 200, 300).")
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")

        # try:
        #     session_data = FinancialData()
            
        #     # Prevent NumPy crash if the user just hits 'enter' and the list is empty
        #     if not session_data.clean_data:
        #         print("Error: No valid data entered. Please enter numbers separated by commas.")
        #         return # Exits this function cleanly without crashing
                
        #     fintraa_calc = StatisticsCalculator(session_data.clean_data)
        #     fintraa_calc.display_all_stats()
            
        # except ValueError:
        #     print("Error: Invalid input. Please only enter numbers (e.g., 100, 200, 300).")
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")

    # --- SETTINGS DISPLAY ONLY ---
    elif choice == 'S':
        print("\n=== FINTRAA KEY MAP & SETTINGS ===")
        show_settings()
        
    # --- CATCH-ALL FOR BAD MAIN MENU INPUTS ---
    else:
        print(f"\nInvalid key [{choice}]! Fintraa automation terminated.")


def run_app():
    print('===============================')
    print('')
    
    # 1. Welcome banner & get username
    username = information()
    
    print('===============================')
    print('')
    
    # 2. Main Menu Choice
    print('Q for MS/Google plugins')
    print('C for Calculator') 
    print('S for Settings')      
    print('===============================')
    
    # Pass the choice into the logic function as an argument
    main_choice = input('''Today's Agenda? : ''').upper()
    logic_choice(main_choice)


# --- Execution Guard ---
# This ensures the script only runs when executed directly.
if __name__ == "__main__":
    run_app()