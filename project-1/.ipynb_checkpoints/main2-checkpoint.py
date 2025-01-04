from banking import *
# from rich.console import Console
# from rich.panel import Panel


# def display_intro():
#     """Displays the introduction with professional formatting."""
#     intro_panel = Panel.fit(
#         """
# [bold yellow]Simulator[/bold yellow]
# [cyan]Submitted to:[/cyan] Dr. Shaista Raees

# [green]The group members are:[/green]
# [b]Muhammad Azzam Hussain[/b] (B21110006068)
# [b]Muhammad Huzaifa Abid[/b] (B21110006077)
# [b]Muhammad Yaseen Azam[/b] (B21110006091)
# [b]Muhammad Laraib[/b] (B21110006081)
# [b]Syed Muhammad Own Hassan[/b] (B21110006134)
# """,
#         title="[bold green]Welcome to the Simulation Program[/bold green]",
#         border_style="blue",
#     )
#     Console.print(intro_panel)


while True:
    # display_intro()
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
