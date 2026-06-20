from abc import ABC


# Parent Class
class BankAccount(ABC):
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(f"₦{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount

    def get_balance(self):
        return self.balance


# Child Class
class SavingsAccount(BankAccount):
    MINIMUM_BALANCE = 5000

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if self.balance - amount < self.MINIMUM_BALANCE:
            raise ValueError(
                f"Withdrawal denied! Savings Account must maintain a minimum balance of ₦{self.MINIMUM_BALANCE}."
            )

        self.balance -= amount
        print(f"₦{amount} withdrawn successfully.")

    
