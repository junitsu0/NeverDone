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
# Ante = Blind
# Deal 5 cards to Community hidden, grp of 3 (flop), grp of 2(river)
# Deal 2 Cards each player and Dealer
# View your hand
# Bet Play (:compared to Ante) 3:1 or 4:1 or Check
# Reveal Flop
# Bet Play 2:1 or Check
# Reveal River
# Bet Play 1:1 or Fold
# Compare Hands and payout
# =============================================================
# Bets - Ante/Play 1:1, Blind/Trips {odds}
# =============================================================
# Blind
# =============================================================
# Royal Flush 500:1
# Straight Flush 50:1
# 4 of a Kind 10:1
# Full House 3:1
# Flush 3:2
# Straight 1:1
# Other PUSH
# =============================================================
# Trips
# =============================================================
# Royal Flush 50:1
# Straight Flush 40:1
# 4 of a Kind 30:1
# Full House 8:1
# Flush 6:1
# Straight 5:1
# 3 of a Kind 3:1
# 