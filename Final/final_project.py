# Template for Final Project
from Final.CPU import CpuPlayer


import argparse 

def parse_args(arglist):

   """Process command line arguments. 

   Args: 
       arglist (list of str): arguments from the command line.

   Returns: 

       namespace: the parsed arguments, as a namespace."""

   parser = argparse.ArgumentParser()

   parser.add_argument("player_name", help = "provide players name")
   parser.add_argument("computer_players", type = int, default = 0, help = "provide an optional integer value representing number of computer players")
   
   return parser.parse_args(arglist)

from Banahene_Game_Class import Deck 
from Banahene_Game_Class import Game
from Bado_Deliverable import Player
from Bado_Deliverable import HumanPlayer
from Zachariah_Deliverable import Turn
#parse args here

if __name__ == "__main__":
    pass
    #define player classes with arg info
    # call game method with players as input
