import sys

class FrontEndSystem:
    def __init__(self):
        self.session_type = None
        self.logged_in = False
        self.transaction_logger = TransactionLogger()

    def start_session(self, session_type):
        self.session_type = session_type
        self.logged_in = True
        print(f"Session started as {self.session_type}")

    def process_transaction(self, transaction_code, *args):
        if not self.logged_in:
            print("Error: You must log in before performing any transactions.")
            return

        if transaction_code == "login":
            if Login().authenticate_user(*args):
                print("Login successful.")
                
                # **Transaction Menu Appears Here**
                print("\n===== Available Transactions =====")
                print("01 - Withdrawal")
                print("02 - Transfer")
                print("03 - Pay Bill")
                print("04 - Deposit")
                print("05 - Create Account")
                print("06 - Delete Account")
                print("07 - Disable Account")
                print("08 - Change Plan")
                print("00 - End of Session\n")
                
            else:
                print("Error: Invalid login credentials.")
        elif transaction_code == "withdraw":
            Withdraw().withdraw_amount(*args)
        elif transaction_code == "transfer":
            Transfer().transfer_funds(*args)
        elif transaction_code == "paybill":
            PayBill().pay_bill(*args)
        elif transaction_code == "deposit":
            Deposit().deposit_funds(*args)
        elif transaction_code == "create":
            CreateAccount().create_new_account(*args)
        elif transaction_code == "delete":
            DeleteAccount().remove_account(*args)
        elif transaction_code == "disable":
            DisableAccount().disable_bank_account(*args)
        elif transaction_code == "changeplan":
            ChangePlan().change_transaction_plan(*args)
        elif transaction_code == "logout":
            self.end_session()
        else:
            print(f"Error: Invalid transaction code {transaction_code}")

    def end_session(self):
        self.logged_in = False
        self.session_type = None
        print("Session ended.")

class TransactionLogger:
    def log_transaction(self, transaction_code, account_number, amount):
        print(f"Logging transaction: {transaction_code} for account {account_number} with amount {amount}")

class Login:
    def authenticate_user(self, session_type, account_name=None):
        print(f"Logging in as {session_type} user")
        valid_standard_users = ["standard_user", "john_doe", "jane_doe"]

        if session_type == "admin":
            return True
        elif session_type == "standard" and account_name in valid_standard_users:
            return True
        else:
            return False

class Withdraw:
    def withdraw_amount(self, account_number, amount, account_balance):
        if amount > 500:
            print("Error: Withdrawal limit exceeded. The maximum withdrawal amount is $500.00 for standard users.")
            return
        if amount > account_balance:
            print("Error: Insufficient balance. Your account balance is lower than the withdrawal amount.")
            return
        account_balance -= amount
        print(f"Successfully withdrew ${amount}. Updated account balance is ${account_balance}")

class Transfer:
    def transfer_funds(self, from_account, to_account, amount):
        print(f"Transferring ${amount} from account {from_account} to account {to_account}")
        print("Transfer completed.")

class PayBill:
    def pay_bill(self, account_number, biller, amount):
        print(f"Paying ${amount} to {biller} from account {account_number}")
        print("Bill payment completed.")

class Deposit:
    def deposit_funds(self, account_number, amount):
        print(f"Depositing ${amount} into account {account_number}")
        print(f"Deposit of ${amount} completed.")

class CreateAccount:
    def create_new_account(self, account_holder_name, initial_balance):
        print(f"Creating a new account for {account_holder_name} with an initial balance of ${initial_balance}")
        print("Account created successfully.")

class DeleteAccount:
    def remove_account(self, account_number):
        print(f"Deleting account {account_number}")
        print("Account deleted successfully.")

class DisableAccount:
    def disable_bank_account(self, account_number):
        print(f"Disabling account {account_number}")
        print("Account disabled.")

class ChangePlan:
    def change_transaction_plan(self, account_number, plan_type):
        print(f"Changing plan for account {account_number} to {plan_type}")
        print(f"Plan changed to {plan_type}.")

# Creating an instance of FrontEndSystem
frontend = FrontEndSystem()

# Start a session (could be "standard" or "admin")
frontend.start_session("standard")

# Perform a login
frontend.process_transaction("login", "standard", "standard_user")

# Attempting a withdrawal
frontend.process_transaction("withdraw", "12345", 100, 500)

# Attempting a transfer
#frontend.process_transaction("transfer", "12345", "67890", 200)

# Attempting a bill payment
#frontend.process_transaction("paybill", "12345", "The Bright Light Electric Company", 50)

# Attempting a deposit
#frontend.process_transaction("deposit", "12345", 100)

# Create a new account
#frontend.process_transaction("create", "Jane Doe", 500)

# Disable an account
#frontend.process_transaction("disable", "12345")

# Change the plan for an account
#frontend.process_transaction("changeplan", "12345", "NP")

# End the session
frontend.end_session()
