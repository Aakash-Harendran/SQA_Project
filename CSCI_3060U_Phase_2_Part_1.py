class FrontEndSystem:
    def init(self):
        self.session_type = None
        self.logged_in = False
        self.transaction_logger = TransactionLogger()

    def start_session(self, session_type):
        self.session_type = session_type
        self.logged_in = True
        print(f"Session started as {self.session_type}")

    def process_transaction(self, transaction_code, args):
        if not self.logged_in:
            print("Error: You must log in before performing any transactions.")
            return

        if transaction_code == "login":
            Login().authenticate_user(args)
        elif transaction_code == "withdraw":
            Withdraw().withdraw_amount(args)
        elif transaction_code == "transfer":
            Transfer().transfer_funds(args)
        elif transaction_code == "paybill":
            PayBill().pay_bill(args)
        elif transaction_code == "deposit":
            Deposit().deposit_funds(args)
        elif transaction_code == "create":
            CreateAccount().create_new_account(args)
        elif transaction_code == "delete":
            DeleteAccount().remove_account(args)
        elif transaction_code == "disable":
            DisableAccount().disable_bank_account(args)
        elif transaction_code == "changeplan":
            ChangePlan().change_transaction_plan(args)
        elif transaction_code == "logout":
            self.end_session()
        else:
            print(f"Error: Invalid transaction code {transaction_code}")