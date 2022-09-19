import random
#api base link --
#https://www.deckofcardsapi.com/api/deck/

#attributes
suits = ('Spades', 'Diamonds', 'Clubs', 'Hearts')
symbols = {'Spades':'\u2664', 'Diamonds':'\u2661', 'Clubs':'\u2667', 'Hearts':'\u2662'}
ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
cardcounts = {'2':+1, '3':+1, '4':+1, '5':+1, '6':+1, '7':0, '8':0, '9':0, '10':-1, 'Jack':-1, 'Queen':-1, 'King':-1, 'Ace':-1}
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

# =============================================================
# Ante
# Deal 5 cards to each player and then Dealer hidden with 1 card visible
# View your hand
# Bet Play (:compared to Ante) 1:1 or 2:1 or 3:1 or fold
# Flip all cards, check results and pay
# =============================================================
# Bets - Ante/Play 1:1, Pair Plus & 6-Card {odds}
# =============================================================
# Ante Bonus
# =============================================================
# 4 of a Kind 25:1
# Straight Flush 20:1
# 3 of a Kind 2:1
# =============================================================
# Aces Up
# =============================================================
# 4 of a Kind 50:1
# Straight Flush 30:1
# 3 of a Kind 7:1
# Flush 6:1
# Straight 5:1
# 2 Pair 2:1
# Pair Aces 1:1
#
#