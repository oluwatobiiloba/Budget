import pandas as pd
indentation="|" * 20
asterisk = "*" * 20
forward='>' *20
backward = '<' *20
class Budget:

    '''This is a class budget'''

    def __init__(self, name, numofcategories, total_budget):
        
        self.name = name
        self.numofcategories = numofcategories
        self.total_budget = total_budget
        

    def totalbudget():
        '''THIS IS THE TOTAL BUDGET METHOD'''
        total_budget = sum(list(categories.category_data.values()))
        return total_budget

    def number_of_categories():
        number_of_categories = len(categories.category_names)
        return number_of_categories

    def main():

        #App startup
        print(indentation + "WELCOME TO YOUR BUDGET APP" + indentation)
        if not categories.category_names:
            print("You currently have no catergories")
            categories.newcategories()
        else:
            categories_landing


class categories(Budget):
    '''THIS IS THE CATEGORIES CLASS'''
    category_names = []
    category_data = {}

    def __init__(self, category_names, category_data):
        super().__init__(name, numofcategories, total_budget)
        self.category_names = category_names
        self.category_data = category_data
        self.total_budget = total_budget
        self.numofcategories= number_of_categories

    def newcategories():
        '''THIS METHOD CREATES NEW CATEGORIES'''
        print(asterisk +"Creating categories" + asterisk)
        category_names_input = [str(category_names_input) for category_names_input in input(
            "Enter Your Category Names (seperate each category with a comma):\n").upper().split(',',)]
        categories.category_names = category_names_input
        initial_amount = 0

        for category in categories.category_names:
           categories.category_data[category] = 0
        # print(categories.category_data)
        categories.categories_landing()

    def categories_landing():
        '''THIS METHOD DIPLAYS THE USERS CATEGORIES IN A DASHBOARD'''
        print("WELCOME TO YOUR DASHBOARD")
        print("YOUR TOTAL BUDGET BALANCE IS %s WITH %s CATEGORIES" %(categories.totalbudget(),categories.number_of_categories()))
        headers = [""]
        print(pd.DataFrame(categories.category_data,
            headers).transpose().rename_axis("CATEGORY"))
        print("Please select a category")
        print(categories.category_data.keys())
        category_selection = str(input("Enter category name:\n").upper())

        if category_selection in categories.category_data.keys():
            print("You selected %s" % category_selection.upper())
            categories.category_ops(category_selection)
        else:
            print("Invalid Selection")
            categories.categories_landing()

    def category_ops(category):
        '''THIS METHOD RUNS ALL CATEGORY OPERATIONS'''
        print("Please Select an operation from the available options:\n 1. DEPOSIT TO %s \n 2. WITHDRAW FROM %s \n 3. %s BALANCE\n 4. TRANSFER\n 5. DASHBOARD\n 6. CREATE NEW CATEGORY" % (
            category, category, category))
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
        '''THIS METHOD DEPOSITS INTO CATEGORIES'''
        depamount = int(
            input("How much do you want to deposit from to %s:\n >>>>" % category))
        categories.category_data[category] += depamount
        print("Deposit successful, Return to dashboard")
        categories.categories_landing()

    def withdraw(category):
        '''THIS CATEGORY WITHDRAWS FROM CATEGORIES'''
        withamount = int(
            input("How much do you want to withdraw from %s:\n >>>>" % category))
        if withamount <= categories.category_data[category]:
            categories.category_data[category] -= withamount
            print("Withdrawal successful, Return to dashboard")
        else:
            print("Insufficient balance")
            categories.withdraw(category)
        categories.categories_landing()

    def category_balance(category):
        '''THIS METHOD DISPLAYS CATEGORY BALANCES'''
        print("Your %s balance is %s" %(category, categories.category_data[category]))
        print("Returning to Dashboard")
        categories.categories_landing()

    def balance_transfer(category):
        '''THIS METHOD TRANSFERS FUNDS BETWEEN CATEGORIES'''
        transamount = int(
            input("Please enter the amount you want to transfer\n>>>"))
        reccat = str(input("Please enter Recipient category\n>>>").upper())
        categories.category_data[category] -= transamount
        if transamount <= categories.category_data[category]:
            if reccat in categories.category_data.keys():
                categories.category_data[reccat] += transamount
                print("You transfered %s from %s to %s " %
                      (transamount, category, reccat))
                categories.categories_landing()
            else:
                print("Category does not exist, retry with existing category ")
                categories.balance_transfer(category)
        else:
            print("Insufficient balance")
            categories.withdraw(category)





#App startup
Budget.main()
