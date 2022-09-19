

class Chips:
    def __init__(self):
        self.total = 500
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

    def blackjack(self):
        self.total += (self.bet * 1.5)

    def surrender(self):
        self.total -= (self.bet * .5)
