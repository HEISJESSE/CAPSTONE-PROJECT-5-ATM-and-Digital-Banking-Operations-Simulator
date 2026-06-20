from datetime import datetime
from transactions import Transaction
from exceptions import BankingError


class MobileBankingGateway:

    def __init__(self):
        self.transactions = []
        self.request_times = []


    # Login/authentication
    def authenticate(self, customer, password):

        if customer.password == password:
            return True

        raise BankingError("Invalid password")



    # Mobile banking transfer
    def transfer(self, sender, receiver, amount):

        self.check_request_limit()


        sender.withdraw(amount)

        receiver.deposit(amount)


        transaction = Transaction(
            sender.account_number,
            "TRANSFER",
            amount,
            datetime.now()
        )


        self.transactions.append(transaction)

        self.request_times.append(datetime.now())


        return transaction



    # Prevent too many transactions
    def check_request_limit(self):

        now = datetime.now()


        recent_requests = [

            t for t in self.request_times

            if (now - t).seconds < 60

        ]


        if len(recent_requests) >= 5:

            raise BankingError(
                "Too many requests. Try again later"
            )



    # Show transaction history
    def get_history(self):

        return self.transactions# To be implemented
