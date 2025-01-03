from banking import *

while True:
    print("Press 1 if you want to create account.")
    print("Press 2 if you want to deposit money in your account.")
    print("Press 3 if you want to withdraw money from your account.")
    print("Press 4 if you want to Check Balance.")
    print("Press 5 if you want to see transactions.")
    print("Press 0 to exit")
    number = int(input("Enter your choice: "))
    if number == 1:
        name = str(input("Enter your name: "))
        if not name.isalpha():  #to check name only contain alphabets
            print("Invalid name. Only alphabets are allowed.")  
        else:
            createAccount(name,accounts,current_id)    
    elif number == 2:
        account_no = input("Enter your account number: ")
        depositMoney(account_no)        
    elif number == 3:
        account_no = input("Enter your account number: ")
        withdrawMoney(account_no)        
    elif number == 4:
        account_no = input("Enter your account number: ")
        checkBalance(account_no)        
    elif number == 5:
        account_no = input("Enter your account number: ")
        printTransactions(account_no)        
    elif number == 0:
        break
    else:
        print("Invalid Choice")
