class CashMachine:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₦{amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ₦{amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current Balance: ₦{self.balance}")
