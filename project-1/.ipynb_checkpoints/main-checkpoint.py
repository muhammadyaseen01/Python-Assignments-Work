
from banking import *
from rich.console import Console
from rich.panel import Panel

console = Console()

def display_intro():
    """Displays the introduction with professional formatting."""
    intro_panel = Panel.fit(
        """
[bold yellow]Banking System[/bold yellow]
[cyan]Submitted to:[/cyan] Sir Nasir Hussain

[green]Created By:[/green]
    [b]Muhammad Yaseen[/b] (334191)
""",
        title="[bold green]Welcome to the Banking System Program[/bold green]",
        border_style="blue",
    )
    console.print(intro_panel)


display_intro()
helper = Panel.fit(
        """
    [bold yellow]This line ensures that the output of each iteration in the while loop appears above it,
                            making it easier to read[/bold yellow]
    """
    )
while True:
    console.print(helper)
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
            current_id += 1    
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

    choice = str(input("you want to do more operations? (yes/no): "))
    if(choice.lower() == "no"):
        break
    else:
        continue