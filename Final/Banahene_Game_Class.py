from random import shuffle

class Deck:
    
    """
    The Deck class creates and manages a deck of 52 cards.
    
    """
    def __init__(self):
        """Initializes a new deck of 52 cards and shuffles it.

        Returns:
            _type_: _description_
        """
        # Create the deck
        self.deck_of_cards = [
            f"{rank} of {suit}"
            for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]
            for rank in ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen", "King"]
        ]
        
        # Shuffle the deck
        shuffle(self.deck_of_cards)
        
class Game:
    def __init__(self, num_players, player_names=None):
        # Create a deck instance/object of a shuffled deck
        d = Deck()
        self.deck_of_cards = d.deck_of_cards
        
        self.num_players = num_players
         
        # Create a list for the player names   
        self.playernames = []
        
        # Default player names if none are provided
        if player_names is None:
                self.playernames.append(f'Human Player')
                for i in range(num_players - 1):
                    self.playernames.append(f'CPU {i + 1}')
                
        if player_names is not None:
            self.playernames = list(player_names)

        # Validate that player_names is a list if provided
        if player_names is not None and not isinstance(player_names, list):
            raise TypeError("The player names must be provided as a list.")
        
        # Validate that the number of player names matches num_players   
        if len(self.playernames) != self.num_players:
            raise ValueError("Invalid number of player names.")        

        
        # Initialize player hands
        self.player_hands = {player: [] for player in self.playernames}
        
        # Distribute cards till deck is empty
        while self.deck_of_cards:
            for player in self.playernames:
                if self.deck_of_cards:
                    self.player_hands[player].append(self.deck_of_cards.pop())
                    
        return self.player_hands
        # Call player_turn
    
        # Call bluff *optional?
        
        # Stop when someone wins
        for player, hand in self.player_hands.items():
            if len(hand) == 0:
                print(f"{player} wins the game!")
                break

        
"""
May be implemented later on

        # Create a list for the player types
        self.playertypes = []

        self.playertypes.append('Human')
        
        for i in range(num_players - 1):
            self.playertypes.append('Computer')
"""