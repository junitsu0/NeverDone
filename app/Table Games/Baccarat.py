import random
import requests
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
#build the deck -want to have 8 decks -416 cards
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
# Bet Banker/Player/Tie/Bonus
# Deal 2 cards Banker Hand and 2 cards Player Hand, no hidden cards
# Draw to Player Hand if necessary
# Draw to Banker Hand if necessary
# Check results and pay
# =============================================================
# Bets - Player 1:1 Banker .95:1, Tie 8:1, Dragon Bonus {odds}
# =============================================================
# Dragon Bonus
# =============================================================
# By 9 30:1
# By 8 10:1
# By 7 6:1
# By 6 4:1
# By 5 2:1
# By 4 1:1
# Natural Win 1:1
# Natural Tie PUSH
# =============================================================