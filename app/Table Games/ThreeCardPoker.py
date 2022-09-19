import random
#api base link --
#https://www.deckofcardsapi.com/api/deck/

#attributes
suits = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
symbols = {'Spades':'\u2664', 'Diamonds':'\u2661', 'Clubs':'\u2667', 'Hearts':'\u2662'}
ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':11}
#use for down below
playing = True
#cards have a rank and suit
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
#build the deck 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        #self.value = 0

    def draw(self, card):
        self.cards.append(card)

class Chips:
    def __init__(self):
        self.total = 500
        self.ante = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

def placebet(chips):

    while True:
        try:
            chips.bet = int(input("Place your ante bet "))
        except ValueError:
            print("Seriously, it's not hard. Try again.")
        else:
            if chips.bet > chips.total or chips.bet == 0:
                print("Oh... you again... you think you are rich, huh?")
            else:
                break

def action(deck, hand):
    global playing

    while True:
        option = input("""
1. Play
2. Fold
        """)
        while option not in {'1', '2'}:
            option = input("Try Again ")           
        if option == '1':
            play(deck, hand)
            print("Player chooses to play the hand")
        elif option == '2':
            print("Player folds")
            playing = False
        else:
            print("Try again")
            continue
        break

def hidden(player, dealer):
    print("\nDealer's Hand:")
    print(" ????????????")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def revealed(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def fold(playhand, chips):
    print("You fold your hand")
    chips.lose()

def push(player, dealer):
    print("Push")

def dealwin(player, dealer, chips):
    print("Dealer wins")
    chips.lose()

def playwin(player, dealer, chips):
    print("Player wins")
    chips.win()

print("Welcome to the Golden Saucer. We only have Blackjack for now.")
print("Change only $500.")
deck = Deck()
deck.shuffle()
chipstack = Chips()

while True:
    player = "Winger"
    playhand = Hand()
    playhand.draw(deck.deal())
    playhand.draw(deck.deal())
    

    dealhand = Hand()
    dealhand.draw(deck.deal())
    dealhand.draw(deck.deal())

    placebet(chipstack)
    hidden(playhand, dealhand)

    while playing:
        action(deck, playhand)
        hidden(playhand, dealhand)

        revealed(playhand, dealhand)

        if dealhand.value > playhand.value:
            dealwin(playhand, dealhand, chipstack)
        elif dealhand.value < playhand.value:
            playwin(playhand, dealhand, chipstack)
        else:
            push(playhand, dealhand)

    print("\nYour chip stack is at $", chipstack.total)

    pressyourluck = input("Keep playing? (y or n) ")

    while pressyourluck not in {'y', 'n'}:
        print("Yes or no, its not hard")
        pressyourluck = input("Focus this time. y or n ")
        if pressyourluck.lower() == 'y':
                print("Well no shit huh")
                playing = True
                continue
        elif pressyourluck.lower() == 'n':
               print("So there is a God")
               break

# =============================================================
# Ante
# Deal 3 cards to each player and then Dealer hidden
# View your hand
# Bet Play equal to Ante or fold
# Flip all cards, check results and pay
# =============================================================
# Bets - Ante/Play 1:1, Pair Plus & 6-Card {odds}
# =============================================================
# Ante Bonus
# =============================================================
# Straight Flush 5:1
# 3 of a Kind 4:1
# Straight 1:1
# =============================================================
# Pair Plus
# =============================================================
# Straight Flush 40:1
# 3 of a Kind 30:1
# Straight 5:1
# Flush 3:1
# Pair 1:1
# =============================================================
# 6 Card Bonus
# =============================================================
# Royal Flush 1000:1
# Straight Flush 200:1
# 4 of a Kind 50:1
# Full House 25:1
# Flush 20:1
# Straight 10:1
# Three of a Kind 5:1
#
#
#