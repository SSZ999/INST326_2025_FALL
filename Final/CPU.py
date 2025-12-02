from Zachariah_Deliverable import Turn
from Bado_Deliverable import Player
class CpuPlayer(Player):
    
    def call_bs():
        return None
    
    def cpu_play(self, req_value):
        """a temporary function, would allow the computer to play cards 
        if playing truthfully
        
        if cpu cannot play truthfully, it will bluff with duplicates in its hand

        Args:
            req_value (int): the turn order value
            cpu_hand (list): the cpu's hand
        
        Returns:
            cpu_play(list): the final hand of the cpu
        
        Side effects:
            will remove selected cards from CPU's hand
        """
        play = []
        while self.deck.count(req_value) != 0:
            play.append(self.deck.pop(index(req_value)))
        if len(play) == 0:
            return [x for x in self.deck if self.deck.count(x) > 1][0]
        return(play)
    
    def cpu_call(self, p_play,req_value):
        """an algoritmn to guess whether or not a player is telling the truth

        Args:
            p_play (list): a list of the subsequent player's input
            req_value (int): the number the player needed to return
        """
        call = True
        possible_options = DECK.copy()
        for i in self.deck:
            possible_options.remove(i)
        
        for i in range(0,len(p_play)):
            try: 
                possible_options.remove(req_value)
            except ValueError:
                call = False
        
        if not call:
            Turn.call_bluff(self.name,p_play,req_value)
        else:
            print("cpu will pass on calling bs")
            self.cpu_play(req_value + 1)
class CpuPlayerComeback(CpuPlayer):
    pass
    def cpu_call(self):
        # if cpu is losing, it will bluff more
        if self.hand == max[self.hand]: #all hands in one list:
            return [x for x in self.deck if self.deck.count(x) > 1][0:2]