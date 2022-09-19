from app import app
from . import Blackjack


@app.route('/')
def index():
    mydeck = Blackjack.Deck()
    return mydeck.deal()
