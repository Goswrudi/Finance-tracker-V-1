# The purpose of this file is to write code for the user weekly reports on credit and debits 
# file under the project of fiinntra...

# Writing daily repots first 

from code_class import weekly_reports

weekly_reports()


def daily():
    # 1. Ask for the total number of items first
    items_spend = int(input('On how many things did you spend total? (e.g., 2): '))

    # 2. Loop through each item one by one
    for i in range(items_spend):
        print(f"\n--- Item #{i+1} ---")
        
        # Ask for the category for THIS specific item (F or T)
        where_spend = input('Which category? eg:([F]ood or [T]ransport): ')
        
        # Ask for the money for THIS specific item
        money_spent = input(f'Enter money spent for {where_spend}: ')
        
        print(f'Recorded: You spent {money_spent} on {where_spend}.')

daily()

