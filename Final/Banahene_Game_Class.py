from Deck import Deck
from Bado_Deliverable import HumanPlayer, Player
from Zachariah_Deliverable import Turn

class Game:
    """ The Game class manages the overall game flow."""
    
    def __init__(self, player_objects):
        self.players = player_objects
        
        # Create and shuffle the deck
        self.deck = Deck().cards
        
        # intitalize turn manager (handles center pile & bluff logic)
        self.manage_turns = Turn()
        
        #Deal cards to players
        self.deal_cards()
    
    def deal_cards(self):
        """Deals cards to players one at a time until the deck is empty."""
        player_index = 0

        while self.deck:
            card = self.deck.pop()
            self.players[player_index].deck.append(card)
            
            # cycle through players
            player_index += 1
            if player_index >= len(self.players):
                player_index = 0
                

    def play(self):
        """Starts the game loop."""
        previous_claim = None
        player_index = 0
        
        while True:            
            # print previous player's claim
            if previous_claim:
                print(f"Previous player's claim: {previous_claim}")
            
            # Current player's turn
            player = self.players[player_index]
            print(f"\n{player.name}'s turn.")
            
            # print player's hand
            print(f"Your current hand is: {player.deck}")

            # Current player makes a move
            claimed_cards = player.turn(self, player.name, player.deck)
            self.manage_turns.center_pile.extend(claimed_cards)
            previous_claim = claimed_cards
            
            # Check if the current player has won
            if len(player.deck) == 0:
                print(f"{player.name} wins the game!")
                return
            
            # Other players can call bluff
            for i in range(len(self.players)):
                if i != player_index:
                    other_player = self.players[i]
                    doubt = input(f"{other_player.name}, do you doubt {player.name}'s claim? (Y/N): ")
                    if doubt.upper() == 'Y':
                        self.manage_turns.call_bluff(other_player, None, player, claimed_cards)
                        break
                    
            # Move to the next player
            player_index = (player_index + 1) % len(self.players)
            
