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
#build the deck -want to have 6 decks -312 cards
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
        self.value = 0
        self.aces = 0

    def draw(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

#checks for aces in hand to reduce if over 21
    def acecheck(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

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

def placebet(chips):

    while True:
        try:
            chips.bet = int(input("Place your bet "))
        except ValueError:
            print("Seriously, it's not hard. Try again.")
        else:
            if chips.bet > chips.total:
                print("Oh... you again... you think you are rich, huh?")
            else:
                break

def hit(deck, hand):
    hand.draw(deck.deal())
    hand.acecheck()

def action(deck, hand):
    global playing

    while True:
        option = input("""
1. Hit
2. Stand
3. Surrender
        """)
        while option not in {'1', '2', '3'}:
            option = input("Try Again ")           
        if option == '1':
            hit(deck, hand)
            print("Player hits")
        elif option == '2':
            print("Player stands")
            playing = False
        elif option == '3':
            surrenderloss(playhand, chipstack.total)
            playing = False
        else:
            print("Try again")
            continue
        break

def holecard(player, dealer):
    print("\nDealer's Hand:")
    print(" ????????????")
    print("Dealer is showing a", dealer.cards[0])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def holereaveled(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def playbust(player, dealer, chips):
    print("Player busts")
    chips.lose()

def playwin(player, dealer, chips):
    print("Player wins")
    chips.win()

def dealbust(player, dealer, chips):
    print("Dealer busts")
    chips.win()

def dealwin(player, dealer, chips):
    print("Dealer wins")
    chips.lose()

def blackjackwin(player, dealer, chips):
    print("BLACKJACK!!! YOU WIN")
    chips.blackjack()

def push(player, dealer):
    print("Push")

def surrenderloss(playhand, chips):
    print("You surrender your hand")
    chips.surrender()



print("Welcome to the Golden Saucer. We only have Blackjack for now.")
print("Change only $500.")
deck = Deck()
deck.shuffle()
chipstack = Chips()

while True:
    #to shuffle a new deck if its below length "-type Deck has no length"
    #if len(deck) < 40:
    #   deck = Deck()
    #   random.shuffle(deck)
    #else:
    #   continue
    player = "Winger"
    playhand = Hand()
    playhand.draw(deck.deal())
    playhand.draw(deck.deal())
    

    dealhand = Hand()
    dealhand.draw(deck.deal())
    dealhand.draw(deck.deal())

    placebet(chipstack)
    holecard(playhand, dealhand)
#blackjack dealt
    if playhand.value == 21 and dealhand.value ==21:
        push(playhand, dealhand)
        print("\nYour chip stack is at $", chipstack.total)
        continue
    elif playhand.value == 21 and dealhand.value != 21:
        blackjackwin(playhand, dealhand, chipstack)
        print("\nYour chip stack is at $", chipstack.total)
        continue
    elif dealhand.value == 21 and playhand.value != 21:
        print("Dealer Blackjack. Sorry Friend.")
        dealwin(playhand, dealhand, chipstack)
        print("\nYour chip stack is at $", chipstack.total)
        continue

    while playing:
        action(deck, playhand)
        holecard(playhand, dealhand)

        if playhand.value > 21:
            playbust(playhand, dealhand, chipstack)
            break

    if playhand.value <= 21:

        while dealhand.value < 17:
            hit(deck, dealhand)

        holereaveled(playhand, dealhand)

        if dealhand.value > 21:
            dealbust(playhand, dealhand, chipstack)
        elif dealhand.value > playhand.value:
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
        while pressyourluck not in {'y', 'n'}:
            print("Are you fucking kidding me right now?")
            pressyourluck = input("They are in caps now, can't miss it. Y or N ")    
            if pressyourluck.lower() == 'y':
                print("Well no shit huh")
                playing = True
                continue
            elif pressyourluck.lower() == 'n':
                print("So there is a God")
                break
    if pressyourluck.lower() == 'y':
        print("Bringin' the heat")
        playing = True
        continue
    elif pressyourluck.lower() == 'n':
        print("Fine go, you stayed your hour")
        break
        