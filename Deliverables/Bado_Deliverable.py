def turn(p_name, p_hand):
    """Manage turns for each player in a BS session.
    
    Args:
        p_name (str): name of the current player
        P_hand (list): current player's set of cards
        
    Side Effects:
        Appends player's played cards to the pile list
        Appends player's proclaimed cards to the p_play list
        
    Returns:
        None
    """
    
    #Checks if card is first in the deck (implied by Ace) to prompt bluff check
    #or not
    while len(p_hand) != 0:
        if pile[-1] != "Ace":
            try:
                bluff_prompt = input(f"Do you doubt {p2_name}'s play? (Y/N)")
                if bluff_prompt == "Y":
                    checking_bluff(p1_name, p1_hand, p2_hand, p2_cards_played,
                                   req_value, pile)
                elif bluff_prompt == "N":
                    continue
            except:
                print("Enter a valid answer.")
                turn(p_name, p_hand)
         
        #Prints player's current hand and asks them to place cards on the deck
        #(Only the current player knows what cards they actually put)       
        print(p_hand)
        play = input(f"{p_name}, please pick no more than 4" 
                     "cards to play: ").strip().split()
        for card in play:
            p_hand.pop(card)
            pile.append(card)
        
        print(f"Your hand is now: {p_hand}")    
        
        #Asks player to state which cards they want the players to think they
        #put down
        claim = input(f"{p_name}, indicate what cards you will"
              "tell other players you put down: ").strip().split()
        for card in claim:
            p_play.append(card)
        
        print(f"{p_name} put down the following cards: {p_play}")
        
        #Checks if current player got rid of all their cards and prints
        #a statement if so
        if len(p_hand) == 0:
            print(f"{p_name} got rid of all their cards and won!")                   