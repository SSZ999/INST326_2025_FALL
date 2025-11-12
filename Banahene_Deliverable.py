from random import shuffle

def deal_cards (players):
    """The deal cards class shuffles a deck of 52 cards and deals cards one by 
    one to each player in the game.

    Args:
        players (list): A list filled with players names.

    Returns:
        dict: A dictionary of the players names and their cards
    """
    
    #Use list comprehension to create a deck of 52 cards
    deck_of_cards = [
        f"{rank} of {suit}"
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]
        for rank in ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen", "King"]
    ]
    
    #Use shuffle from random module to randomize the cards
    shuffle(deck_of_cards)
    
    #initalize hands for each player
    player_hand = {player: [] for player in players}
    
    #Split shuffled deck amongst player #, 1 by 1 until deck is empty
    while deck_of_cards:
        for player in players:
            if deck_of_cards:
                player_hand[player].append(deck_of_cards.pop()) 
    
    #Return a dictionary of all the players hands
    return player_hand

#Made up data for the function to take:
players = ["Elizabeth","Megan","Seniah","Henry"]

#Call the function to see the hand of a specific player
hands = deal_cards(players)
print(hands["Elizabeth"])