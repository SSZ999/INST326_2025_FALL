from random import shuffle

class Deck:
    """ The Deck class creates and manages a deck of 52 cards."""
    
    def __init__(self):
        """Initializes a new deck of 52 cards and shuffles it.
        """
        
        # Create the deck
        self.cards = [
            f"{rank} of {suit}"
            for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]
            for rank in ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen", "King"]
        ]
        
        # Shuffle the deck
        shuffle(self.cards)