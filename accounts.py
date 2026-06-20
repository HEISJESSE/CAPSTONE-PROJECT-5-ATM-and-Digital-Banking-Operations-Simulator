# Parent Class
class BankAccount(ABC):
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"₦{amount} deposited successfully.")

    @abstractmethod
    def withdraw(self, amount):
        pass


# Child Class
class SavingsAccount(BankAccount):
    MINIMUM_BALANCE = 5000

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if self.balance - amount < self.MINIMUM_BALANCE:
            raise ValueError(
                f"Withdrawal denied! Account balance cannot go below ₦{self.MINIMUM_BALANCE}."
            )

        self.balance -= amount
        print(f"₦{amount} withdrawn successfully.")


# Test Code
if __name__ == "__main__":
    account = SavingsAccount("2024154094", 20000)

    print(f"Initial Balance: ₦{account.balance}")

    account.deposit(5000)
    print(f"Balance after deposit: ₦{account.balance}")

    account.withdraw(10000)
    print(f"Balance after withdrawal: ₦{account.balance}")

    # This will raise an error
    account.withdraw(11000)
