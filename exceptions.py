class BankingError(Exception):
    pass

class InsufficientFundsError(BankingError):
    pass

class DailyLimitExceededError(BankingError):
    pass

class CardBlockedError(BankingError):
    pass

class FraudSuspicionError(BankingError):
    pass
