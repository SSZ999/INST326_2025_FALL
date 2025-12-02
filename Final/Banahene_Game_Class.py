from Deck import Deck
from Bado_Deliverable import HumanPlayer, Player

class Game:
    """ The Game class manages the overall game flow."""
    
    def __init__(self, player_objects):
        self.players = player_objects
        
        # Create and shuffle the deck
        self.deck = Deck().cards
        
        # Create a deck object and store it
        self.center_pile = []
        
        #Deal cards to players
        self.deal_cards()
    
    def deal_cards(self):
        """Deals cards to players until the deck is empty."""
        player_index = 0

        while self.deck:
            # give each player 1 card at a time
            card = self.deck.pop()
            self.players[player_index].deck.append(card)
            
            # cycle through players
            player_index += 1
            if player_index >= len(self.players):
                player_index = 0
                

    def start_game(self):
        """Starts the game loop."""
        previous_claim = None
        
        while True:
            for player in self.player:
                print(f"\n{player.name}'s turn.")
                claim = player.turn(self.center_pile, player.name, player.deck, previous_claim)
                
                # Update previous claim
                previous_claim = claim
                
                # Check for win condition
                if len(player.deck) == 0:
                    print(f"{player.name} wins the game!")
                    return
                
RANDOMMMMM

class Game:
    """ The Game class manages the overall game flow."""
    
    def __init__(self, num_players, player_names=None):
        self.num_players = num_players
        self.pla
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
    def

        
"""
May be implemented later on

        # Create a list for the player types
        self.playertypes = []

        self.playertypes.append('Human')
        
        for i in range(num_players - 1):
            self.playertypes.append('Computer')
"""