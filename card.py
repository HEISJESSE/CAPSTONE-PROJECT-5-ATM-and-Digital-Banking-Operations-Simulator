class ATMCard:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.blocked = False

    def verify_pin(self, entered_pin):
        if self.blocked:
            return False
        return self.pin == entered_pin

    def block(self):
        self.blocked = True

    def unblock(self):
        self.blocked = False
