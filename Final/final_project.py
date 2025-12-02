# Template for Final Project
from Final.CPU import CpuPlayer
from Banahene_Game_Class import Deck, Game
from Bado_Deliverable import Player, HumanPlayer
from Zachariah_Deliverable import Turn
#parse args here

from argparse import ArgumentParser
from sys import argv

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

def main(args):
    Game(int(args.computer_players),args.player_name)
    
if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args)
