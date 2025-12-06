import random

class Turn:
    """An object that represents a turn"""

    
    def deal_cards(self, game):
        """deal out deck of cards equally among players
        
        Args:
            game(Game): game object
        
        Side effects:
            updates players hands with equal amount of cards"""
        player_index = 0

        while game.deck:
            #game.players should be a list of total player objects
            card = game.deck.pop()
            game.players[player_index].hand.append(card)

            player_index += 1
            if player_index >= len(game.players):
                player_index = 0

    def distribute_cards(self,game, player):
        """distributes card pile to losing player based on if bluff call was right or wrong
        Args:
            player(Player): player object, which is the losing player
        Side effects:
            updates losing players hand with pile of cards"""
        while game.center_pile:
            card = game.center_pile.pop()
            player.hand.append(card)

    def win_check(self, player):
        """determines if a player has won
        Args:
            player(Player): player object 
        Side effects:
            if a player has won it prints results to console 
            """
        if len(player.hand) == 0:
            print(f"{player.name} won!")

    def call_bluff(self,game,accuser, accused, req_value, played_cards):
        """Checks if player2 was bluffing based on required value they were supposed to play
        
        Args:
            game(Game): game class object 
            accuser(Player): player who is accusing another player of bluffing    
            accused(Player): player who is being accused of bluffing  
            req_value(int or str): required value of cards that accused player was supppsed to put down
            played_cards(list): cards that the accused player played when bluff was called
        Side effects:
            updates center pile to include accused players cards that were called bluff on 
            if accused player was bluffing, their hand gets updated as they take the pile of cards
            if accused player was not bluffing, the accusers hand gets updated as they take the pile of cards
            print the results of bluff to console 
            
            """
        #accuser and accused are player objects 
        #played cards are the cards the accuser played that was called bs on

        lied = False
        for card in game.played_cards:
            if card != game.req_value:
                lied = True
                break

        if lied:
            print(f"{accused.name} lied and has to take the pile!")
            self.distribute_cards(accused)
        else:
            print(f"{accuser.name} called bs and was wrong and has to take the pile!")
            self.distribute_cards(accuser)
            
            