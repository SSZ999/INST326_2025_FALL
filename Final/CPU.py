"""
cpu class 

thinks about the future

            determines if cpu should bluff, calls cpu_bluff

            returns list that cpu will play for required number

        cpu_bluff
            calculates most probable bluff, what cards to substitute as what

        cpu_call_bluff x 
            has a simulated list of cards outside the computer's hand as well as
            the center hand

            when a player places a card, the computer can simulate that card's 
            probability in relation to it's knowledge of what is 'outside'

            returns True/False for bs/no bs
"""

class CpuPlayer:
    def __init__(self,hand):
        self.hand = hand
    
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
        while self.hand.count(req_value) != 0:
            play.append(self.hand.pop(index(req_value)))
        if len(play) == 0:
            return [x for x in self.hand if self.hand.count(x) > 1][0]
        return(play)
    
    def cpu_call(self, p_play,req_value):
        """an algoritmn to guess whether or not a player is telling the truth

        Args:
            p_play (list): a list of the subsequent player's input
            req_value (int): the number the player needed to return
        """
        call = True
        possible_options = DECK.copy()
        for i in self.hand:
            possible_options.remove(i)
        
        for i in range(0,len(p_play)):
            try: 
                possible_options.remove(req_value)
            except ValueError:
                call = False
        
        if not call:
            call_bs("cpu",p_play,req_value)
        else:
            print("cpu will pass on calling bs")
            cpu_play(req_value + 1)
class CpuPlayerComeback(CpuPlayer):
    pass
    def cpu_call(self):
        # if cpu is losing, it will bluff more
        if self.hand == max[self.hand] #all hands in one list:
            return [x for x in self.hand if self.hand.count(x) > 1][0:2]