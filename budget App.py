import pandas as pd
class Budget:
    
    '''This is a class budget'''
    def __init__(self,name,numofcategories,total_budget):
        self.name = name
        self.numofcategories = numofcategories
        self.total_budget = total_budget
    
    def totalbudget():
        total_budget = sum(list(categories.category_data.values()))
        return total_budget


    

class categories(Budget):
    category_names = []
    category_data = {}
    
    def __init__(self, category_names, category_data):
        super().__init__(name, numofcategories, total_budget)
        '''this is the category class'''
        self.category_names = category_names
        self.category_data = category_data
        self.total_budget = total_budget
        total_budget = sum(list(categories.category_data.values()))
  
    def newcategories():
        print("Creating categories")
        category_names_input = [str (category_names_input) for category_names_input in input("Enter category names with a comma seperator:").upper().split(',',)]
        categories.category_names = category_names_input
        initial_amount = 0
        
        for category in categories.category_names:
           categories.category_data[category] = 0
        # print(categories.category_data)
        categories.categories_landing()
        
    def categories_landing():
        print("WELCOME TO YOUR DASHBOARD")
        print("YOUR TOTAL BUDGET BALANCE IS %s" %categories.totalbudget()  )
        headers= [""]
        print(pd.DataFrame(categories.category_data,headers).transpose().rename_axis("CATEGORY"))
        print("Please select a category")
        print(categories.category_data.keys())
        category_selection =  str(input("Enter category name:\n").upper())
        
        if category_selection in categories.category_data.keys():
            print("You selected %s" %category_selection.upper())
            categories.category_ops(category_selection)
        else:
            print("Invalid Selection")
            categories.categories_landing()
          
                
                
    def category_ops(category):
        print("Please Select an operation from the available options:\n 1. DEPOSIT TO %s \n 2. WITHDRAW FROM %s \n 3. %s BALANCE\n 4. TRANSFER\n 5. DASHBOARD\n 6. CREATE NEW CATEGORY" %(category,category,category))
        ops = int(input(">>>>"))
        if ops == 1:
            categories.deposit(category)
        elif ops == 2:
            categories.withdraw(category)
        elif ops == 3:
            categories.category_balance(category)
        elif ops == 4:
            categories.balance_transfer(category)
        elif ops == 5:
            main()
        elif ops == 6:
            categories.newcategories()     
        else:
            print("Enter valid selection")
            categories.category_ops(category_selection)

    def deposit(category):
        
        depamount = int(input("How much do you want to deposit from to %s:\n >>>>" %category))
        categories.category_data[category] += depamount
        print("Deposit successful, Return to dashboard")
        categories.categories_landing()
        
    def withdraw(category):
        withamount = int(input("How much do you want to withdraw from %s:\n >>>>" %category))
        if withamount <= categories.category_data[category]:
            categories.category_data[category] -= withamount
            print("Withdrawal successful, Return to dashboard")
        else:
            print("Insufficient balance")
            categories.withdraw(category)
        categories.categories_landing()

    def category_balance(category):
        print("Your %s balance is " %
              (category, categories.category_data[category]))
        print("Returning to Dashboard")
        categories.categories_landing()
    def balance_transfer(category):
        transamount = int(input("Please enter the amount you want to transfer\n>>>"))
        reccat = str(input("Please enter Recipient category\n>>>").upper())
        categories.category_data[category] -= transamount
        if transamount <= categories.category_data[category]:
            if reccat in categories.category_data.keys():
                categories.category_data[reccat] += transamount
                print("You transfered %s from %s to %s " %(transamount,category,reccat))
                categories.categories_landing()
            else:
                print("Category does not exist, retry with existing category ")
                categories.balance_transfer(category)
        else:
            print("Insufficient balance")
            categories.withdraw(category)
    


def main():
    

    #App startup
    print("WELCOME TO ")
    if not categories.category_names:
        print("You currently have not created any catergories")
        categories.newcategories()
    else:
       categories_landing




#App startup
main()
        




