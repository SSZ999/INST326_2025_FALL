import random

class Turn:
    def randomize_deck(self,game):
        shuffled_list = [] 
        for card in game.deck:
            random_card = random.choice(game.deck)
            shuffled_list.append(random_card) 
    
       
        while shuffled_list: 
            for card in game.deck:
                for player in game.player:
                    card_distrubuted = shuffled_list.pop()
                    self.deck.append(card_distrubuted) 
    
    def win_check(self, player):
        if not player.deck:
            print(f"{self.name} won!"})

    
    def distribute_cards(self,player,game):
        #will this have to add the player2s hand or will pile already include it 
        player.deck.append(game.pile)

    
    def checking_bluff(self,game,player1,player2):
        #fix 
        bluff = False
        for card in player2.cards_played:
            if card != req_value:
                bluff = True
                break 
        
        if bluff:
            print(f"{player1.name} called BS and was Correct.")
            distribute_cards(p2_hand,p2_cards_played, pile)
        else:
            print(f"{player1.name} called BS and was Incorrect.") 
            bluff_dealer(p1_hand,p2_cards_played, pile)

        