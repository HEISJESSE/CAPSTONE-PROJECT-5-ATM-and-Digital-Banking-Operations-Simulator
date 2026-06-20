
from datetime import datetime, timedelta
from exceptions import FraudSuspicionError


class FraudDetector:

    def __init__(self):
        self.transaction_log = {}

    def record_transaction(self, account_no):

        current_time = datetime.now()

        if account_no not in self.transaction_log:
            self.transaction_log[account_no] = []

        self.transaction_log[account_no].append(current_time)

    def check_rapid_transactions(self, account_no, card=None):

        current_time = datetime.now()

        transactions = self.transaction_log.get(account_no, [])

        recent_transactions = []

        for t in transactions:
            if current_time - t <= timedelta(seconds=60):
                recent_transactions.append(t)

        self.transaction_log[account_no] = recent_transactions

        if len(recent_transactions) >= 5:

            if card:
                card.block()

            raise FraudSuspicionError(
                "Fraud detected: Too many transactions within 60 seconds"
            )

        return False
