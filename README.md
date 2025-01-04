## project-1 contain two projects, one for notebook and other is made of modules for testing

# Banking System Project

This project is a simple banking system where users can perform operations such as creating an account, depositing money, withdrawing money, checking balance, and printing transaction history. The project consists of two main files:

- `main.py`: This is the main driver file where the user interacts with the banking system.
- `banking.py`: This file contains the functions that handle the core banking operations.

## Files

### `main.py`

This file handles the user interaction and calls the functions defined in `banking.py`. It uses a simple menu system where users can choose various operations:

1. Create a new account
2. Deposit money into an account
3. Withdraw money from an account
4. Check the balance
5. Print transaction history
6. Exit the program

### `banking.py`

This file defines all the functions necessary for performing the banking operations, such as:

- **createAccount()**: Creates a new account with a unique account number.
- **depositMoney()**: Deposits money into a specified account.
- **withdrawMoney()**: Withdraws money from a specified account, ensuring sufficient balance.
- **checkBalance()**: Displays the current balance of an account.
- **printTransactions()**: Prints the transaction history of an account.

## How to Use

1. Clone this repository or download the files.
2. Make sure both `main.py` and `banking.py` are in the same directory.
3. Run the `main.py` file to start interacting with the banking system.

In terminal run this command
python main.py
