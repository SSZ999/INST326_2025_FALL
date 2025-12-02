import random

class Turn:

    def __init__(self):
        self.center_pile = []

    def randomize_deck(self, game):
        random.shuffle(game.deck)

    def deal_cards(self, game):
        player_index = 0

        while game.deck:
            #game.players should be a list of total player objects
            card = game.deck.pop()
            game.players[player_index].deck.append(card)

            player_index += 1
            if player_index >= len(game.players):
                player_index = 0

    def distribute_cards(self, player):
        while self.center_pile:
            card = self.center_pile.pop(0)
            player.deck.append(card)

    def win_check(self, player):
        if len(player.deck) == 0:
            print(f"{player.name} won!")

    def call_bluff(self, accuser, accused, req_value, played_cards):
        #accuser and accused are player objects 
        #played cards are the cards the accuser played that was called bs on

        for card in played_cards:
            self.center_pile.append(card)

        lied = False
        for card in played_cards:
            if card != req_value:
                lied = True
                break

        if lied:
            print(f"{accused.name} lied and has to take the pile!")
            self.distribute_cards(accused)
        else:
            print(f"{accuser.name} called bs and was wrong and has to take the pile!")
            self.distribute_cards(accuser)