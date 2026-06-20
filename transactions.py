 class TransactionProcessor:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₦{amount}")
        print(f"New Balance: ₦{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ₦{amount}")
            print(f"New Balance: ₦{self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Current Balance: ₦{self.balance}")
