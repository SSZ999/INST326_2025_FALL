def bluff_dealer(hand, p2_cards_played, pile):
    """Handles giving cards to losing player. Adds both the cards that were played 
    when bluff was called and rest of card pile. 
    Args:
        hand(list): hand of losing player 
        p2_cards_played(list): player2's cards that were played when bluff was 
        called
        pile(list): pile of cards up till bluff was called
    """
    pass

def checking_bluff(p1_name,p1_hand,p2_hand,p2_cards_played,req_value, pile):
    """Checks if player2 was bluffing based on required value they were supposed
    to play.
    
    Args:
        p1_name(str): player1's name (player who called bluff on player2)
        p1_hand(list): player1's hand
        p2_hand:(list): player2's hand
        p2_cards_played: player2's cards that were played when bluff was called
        req_value(int or str): required value of cards that player2 was supposed 
        to play
        pile(list): pile of cards up till bluff was called
    
    Side effects:
        updates players current hands based on whether BS call was correct or 
        incorrect
        if player2 was not bluffing, player1 takes the pile
        if player2 was bluffing, player2 takes the pile
        prints the results of the bluff to the console  
    
    Returns:
        None 
        
    """
    bluff = False
    for card in p2_cards_played:
        if card != req_value:
            bluff = True
            break 
        
    if bluff:
        print(f"{p1_name} called BS and was Correct.")
        bluff_dealer(p2_hand,p2_cards_played, pile)
    else:
        print(f"{p1_name} called BS and was Incorrect.") 
        bluff_dealer(p1_hand,p2_cards_played, pile)

            