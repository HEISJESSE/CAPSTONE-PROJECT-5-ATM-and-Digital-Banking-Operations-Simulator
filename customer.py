# To be implemented
class ATMCard:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.__pin = pin          # private attribute
        self.blocked = False

    def verify_pin(self, entered_pin):
        if self.blocked:
            return "Card is blocked"

        if entered_pin == self.__pin:
            return True
        else:
            return False

    def block(self):
        self.blocked = True
        return "Card blocked successfully"

    def unblock(self):
        self.blocked = False
        return "Card unblocked successfully"
