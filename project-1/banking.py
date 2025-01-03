accounts = {}
current_id = 0

def generateAccountNo(current_id):
    prefix = "PKYN" # starting of account number
    next_number = str(current_id + 1).zfill(3)  # use three digit id but you can increase it by increasing the number in zfill
    return prefix + next_number


def createAccount(name,accounts,current_id):
    if not name.isalpha():  #to check name only contain alphabets
        print("Invalid name. Only alphabets are allowed.")
        return
    # generating account number and save it in accout_no variable
    account_no = generateAccountNo(current_id)
    # making dictionary to save accounts details
    account_details = {
    "name": name,
    "balance": 0.0,
    "transactions": []
    }
    # saving accounts_details as value and set account_no as key
    accounts[account_no] = account_details
    print(f"Account for {account_details['name']} with account_no {account_no} created with balance $0.0.")
    # print(account['name'])



#############################################################################
#i am not adding limit how much ammount can be deposit in one transaction or in one day
# it is also possible but not mentioned in the question
def depositMoney(account_no):
    if account_no in accounts: #checking weather the account_no is in accounts dict or not
        amount = float(input("enter the amount you want to deposit: "))
        try: # checking for ammount 
            if amount < 0:
                raise ValueError("Negative values are not allowed.")
            elif amount == 0:
                raise ValueError ("Zero value is not allowed")
            # adding amount to balance
            accounts[account_no]["balance"] += amount
            # inserting deposited amount in transaction dictionary of given account number
            accounts[account_no]["transactions"].append(f"Deposit: ${amount}")
            print(f"Amount Deposit: ${amount}")
            print(f"Updated balance: ${accounts[account_no]['balance']}")
            # print(accounts[account_no]['balance'])
            with open("transactions.txt", "a") as f: # open in "a" mode to avoid overwriting
                # writing in the transaction file as per question requirement
                f.write(f"Account No: {account_no}, Transaction: Deposit, Amount: ${amount}, New Balance: ${accounts[account_no]['balance']}\n")
        # to catch error
        except ValueError as e:
            print("Error:", e)
    else:
        print(f"Acoount_no: {account_no} not found!")

# depositMoney('PKYN002')



#############################################################################
#i am not adding limit how much ammount can be withdraw in one transaction or in one day
# it is also possible but not mentioned in the question
def withdrawMoney(account_no):
    if account_no in accounts:#checking weather the account_no is in accounts dict or not
        amount = float(input("enter the amount you want to withdraw: "))
        try:# checking for ammount
            if amount < 0:
                raise ValueError("Negative values are not allowed.")
            elif amount == 0:
                raise ValueError ("Zero value is not allowed")
            # amount should be lesser than current balance
            if amount > accounts[account_no]["balance"]:
                print("Insufficient balance!")
                return

            # detecting amount from current balance
            accounts[account_no]["balance"] -= amount
            # inserting withdrawed amount in transaction dictionary of given account number
            accounts[account_no]["transactions"].append(f"Withdrawn: ${amount}")
            print(f"Amount withdrawn: ${amount}")
            print(f"Updated balance: ${accounts[account_no]['balance']}")
            
        except ValueError as e:
            print("Error:", e)
    else:
        print(f"Acoount_no: {account_no} not found!")
        
# withdrawMoney('PKYN002')

    

#############################################################################
def checkBalance(account_no):
    if account_no in accounts:#checking account no is in dictionary or not
        #printing  current balance for given account number
        print(f"The current balance for account_no: {account_no} is ${accounts[account_no]['balance']}")
    else:
        print("Invalid account no")
# checkBalance('PKYN002')


#############################################################################
def printTransactions(account_no):
    if account_no in accounts:#checking account no is in dictionary or not
        print(f"Transactions for account_no {account_no} are:")
        # transactions may be more than one therefore we use for loop
        for transaction in accounts[account_no]["transactions"]:
            print(transaction)
    else:
        print(f"Account_no: {account_no} not found!")

# printTransactions('PKYN002')
#############################################################################