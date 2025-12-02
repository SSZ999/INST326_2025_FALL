class Player:
    """Base class for BS player
    
    Attributes:
        name (str): player's name
        deck (list): player's deck of cards
    """
    
    def __init__(self, name, deck):
        self.name = name
        self.deck = []
        
    def turn(self):
        raise NotImplementedError
    
class HumanPlayer(Player):
    def turn(self, state, name, deck):
        """Take turn as human player
        
        Args:
            state (GameState): snapshot of current game state
            name (str): name of current turn's player
            deck (list of str): current player's hand
        
        Side Effects:
            Removes selected cards from a player's hand
            Appends cards to the pile
            Appends cards to p_play, the play other players see
        """
    #Checks if card is first in the deck (implied by Ace) to prompt bluff check
    #or not        
        while len(deck) != 0:
            if deck[-1] != "Ace":
                try:
                    doubt = input(f"{name}, do you doubt the "
                                  "last player's play? (Y/N)")
                    if doubt == "Y":
                        return doubt
                    elif doubt == "N":
                        break
                except:
                    print("Enter a valid answer.")
            else:
                break
                    
        #Prints player's current hand and asks them to place cards on the deck
        #(Only the current player knows what cards they actually put) 
        print("Your current hand is " + deck)
        play = input(f"{name}, please pick no more than 4" 
                     "cards to play: ").strip().split()
        for card in play:
            deck.pop(card)
            pile.append(card)
        
        print(f"Your hand is now: {deck}")    
        
        #Asks player to state which cards they want the players to think they
        #put down
        claim = input(f"{name}, indicate what cards you will"
              "tell other players you put down: ").strip().split()
        for card in claim:
            p_play.append(card)
        
        print(f"{name} put down the following cards: {p_play}")
        
        #Checks if current player got rid of all their cards and prints
        #a statement if so
        if len(deck) == 0:
            print(f"{name} got rid of all their cards and won!") 
            
#NOTE: p_play is the variable which represents the player saying what cards
#they put down to the other players; this is what other players will
#reference if they want to call someone's bluff             
