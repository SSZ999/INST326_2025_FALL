# print player hand every round
# add extra cpu
# add headers for rounds
# make cpu dumber
import argparse
import random

# Constants
RANKS = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
COPIES_PER_RANK = 4
MAX_PLAY = 4   # max cards per turn for both CPU & human

# Deck class
class Deck:
    """Deck of 52 cards represented by ranks only. 
    
    Attributes:
        cards (list): list of all cards in the deck
    """
    def __init__(self):
        """Initialize the deck with 52 cards and shuffle them."""
        self.cards = RANKS * COPIES_PER_RANK
        random.shuffle(self.cards)

# Player base class
class Player:
    """Base class for human & CPU players.
    
    Attributes:
        name (str): name of human or CPU player
        deck (list): list of all cards in a human or CPU's hand    
    """
    
    def __init__(self, name):
        """Creates instance of a player, human or CPU
        
        Args:
            name (str): provided name of a BS player
            
        Side Effects:
            Creates an empty list, deck, representing a player's hand
        """
        self.name = name
        self.deck = []

    def __repr__(self):
        return f"<Player {self.name} ({len(self.deck)} cards)>"

    def has_cards(self):
        """Checks if a player has cards in their hand
        
        Returns:
            Boolean statement of if the length of a player's deck is greater
            than zero
        """
        return len(self.deck) > 0

    def remove_cards_by_indices(self, indices):
        """Remove cards by index (descending order) and return them.
        
        Args:
            indices (int): indices for cards in a deck
            
        Side Effects:
            Creates an empty list, selected
            Appends each index into the "selected" list
            Removes specified cards from self.deck
            Reverses "selected" list
            
        Returns:
            "Selected" list containing removed cards
        """
        selected = []
        for idx in sorted(indices, reverse=True):
            selected.append(self.deck.pop(idx))
        selected.reverse()
        return selected


# Human player class
class HumanPlayer(Player):
    """Child class inheriting from the Player class that represents
    a human BS player."""
    
    def take_turn(self, required_rank):
        """Take a turn of BS
        
        Args:
            required_rank (index): the rank player must play
            
        Side Effects:
            Alters value of actual_cards based on which cards a player
            puts down
            Prints player name, required rank, and current player hand
            sorted in ascending order
            Creates variable "n", which is the number of cards the player
            wants to put down (1-4) and is inputted in a print statement
            Creates variable "raw", which is the raw input of the indices a user 
            selects inputs 
            Creates sorted_indices, a list for the inputted indices to be 
            converting into integers and sorted in ascending order
            Creates real_indices, a list of integers representing the indices
            of cards to be removed
            Creates actual_cards, a list, which represents 
            the cards a player used
            
        Returns:
            actual_cards, actual list of cards in player's hand
            required_rank, the rank the next player must put down on their turn
        """
        print(f"\n{self.name}'s turn — Required claim rank: {required_rank}")
        print("Your cards:")
        sorted_hand = sorted(range(len(self.deck)), 
                             key= lambda i: RANKS.index(self.deck[i]))
        for display_i, real_i in enumerate(sorted_hand):
            print(f"[{display_i}] {self.deck[real_i]}", end='  ')
        print("\n")

        while True:
            try:
                n = int(input(f"How many cards do you want to play? "
                              f"(1 to {min(MAX_PLAY, len(self.deck))}): "))
                if 1 <= n <= min(MAX_PLAY, len(self.deck)):
                    break
            except:
                pass
            print("Invalid number.")

        while True:
            raw = input(f"Enter {n} card indices separated by spaces: ").strip()
            parts = raw.split()
            if len(parts) != n:
                print(f"Enter exactly {n} indices.")
                continue

            try:
                sorted_indices = [int(p) for p in parts]
            except:
                print("Indices must be numbers.")
                continue

            if any(i < 0 or i >= len(sorted_hand) for i in sorted_indices):
                print("Index out of range.")
                continue

            break
        
        real_indices = sorted((sorted_hand[i] for i in sorted_indices)
                              , reverse = True)
        actual_cards = self.remove_cards_by_indices(real_indices)
        print(f"{self.name} placed {len(actual_cards)} cards and CLAIMS "
              "they are all {required_rank}.")
        return actual_cards, required_rank

# CPU player class
class CpuPlayer(Player):
    """Child class inheriting from the Player class that represents
    a computer BS player.

    Attributes:
        name (str): name of CPU player, inherited from Player class
        deck (list): all cards in a CPU's hand , inherited from Player class

    """
    def memory_loss(self, rank_positions):
        """Removes cards in cpu's 'memory' when taking a turn

        Args:
            rank_positions (list): the cards a cpu has of the desired rank

        Returns:
            rank_positions: (list): the cards a cpu has of the desired rank
            
        Side effects:
            will remove a random amount of items from rank_positions
        """
        for i in range(0,random.randint(1,len(rank_positions))):
            rank_positions.pop()
        return rank_positions
    
    def take_turn(self, required_rank):
        """determines the computer output when prompted to take a turn

        Args:
            required_rank (int): the required number a computer has to play

        Returns:
            cards (list): the cards the cpu puts down into the center hand
            required_rank (int): rank that will be used to judge if cpu is lying
        
        Side effects:
            prints the cpu's claim
            there is a 50% chance memory_loss() will be called
            removes played cards from cpu's hand
        """
        rank_positions = [i for i,c in enumerate(self.deck) if c == required_rank]

        rank_positions = self.memory_loss(rank_positions) if random.random() == 1.0 else rank_positions
        
        if rank_positions:
            count_to_play = min(len(rank_positions), random.randint(1, min(MAX_PLAY, len(rank_positions))))
            indices = rank_positions[:count_to_play]
            cards = self.remove_cards_by_indices(indices)
            print(f"{self.name} (CPU) plays {len(cards)} cards claiming {required_rank}.")
            return cards, required_rank

        n = min(random.randint(1, MAX_PLAY), len(self.deck))
        indices = random.sample(range(len(self.deck)), n)
        cards = self.remove_cards_by_indices(indices)
        print(f"{self.name} (CPU) plays {len(cards)} cards claiming {required_rank}.")
        return cards, required_rank

    def decide_call_bluff(self, claimed_player, claimed_rank, claimed_count):
        """determines if a computer should call a bluff or not

        Args:
            claimed_player (Player): the Player class that went most recently
            claimed_rank (int): the rank the claimed_player played in
            claimed_count (int): the count of cards the player played

        Returns:
            decision (Boolean): 
                True if CPU thinks claimed_player is lying
                False if CPU thinks claimed_player is telling truth
        Side effects:
            prints whether or not CPU calls BS on claimed_player or not
        """
        own_count = self.deck.count(claimed_rank)
        threshold = COPIES_PER_RANK - own_count

        suspicion = 0.6 if claimed_count > threshold else 0.15
        if len(self.deck) > 10:
            suspicion += 0.05

        decision = random.random() < suspicion

        if decision:
            print(f"{self.name} CALLS BS on {claimed_player.name}!")
        else:
            print(f"{self.name} passes.")

        return decision

# Turn manager class
class TurnManager:
    """An object that represents a turn.
    
    Attributes:
        center_pile(list): initially empty center pile of cards"""
    def __init__(self):
        """Initialize a new TurnManager class object
        
        Side effects:
            Set attribute center_pile.
        """
        self.center_pile = []

    def add_play(self, cards):
        """adds the played cards from a player's turn to the center pile
        
        Args:
            cards(list): cards the player just played
        
        Side effects: 
            modifies the center_pile list by appending the given cards"""
        self.center_pile.extend(cards)

    def resolve_bluff(self, accuser, accused, played_cards, claimed_rank):
        """Evaluate the BS call and determine if the accused player lied or not, 
        if they did then they take the pile of cards, if they didn't then the accuser
        takes the pile of cards.
        
        Args:
            accuser(Player): the player who called BS
            accused(Player): the player whose play is being called bs on
            played_cards(list): the actual cards the accused player played 
            claimed_rank(str): the rank the accused player said they played
        
        Returns:
            taker(Player): the player who loses the BS call and must pick up the
            center pile (the loser of the call)
        
        Side effects:
            appends the played cards to the center pile
            clears the center pile after evaluating the bluff
            adds the pile's cards to the accuser or accused players deck
            prints the outcome of the bluff call"""
        lied = any(card != claimed_rank for card in played_cards)

        taker = accused if lied else accuser 
        
        if lied:
            print(f"{accused.name} LIED and picks up {len(self.center_pile)} cards!")
        else:
            print(f"{accuser.name} was WRONG and picks up {len(self.center_pile)} cards.")
        
        taken = self.center_pile.copy()
        self.center_pile.clear()
        taker.deck.extend(taken)
        
        return taker
# Game engine class
class Game:
    """Game engine to manage the flow of the BS card game.
    
    Attributes:
        players (list): list of Player objects participating in the game
        deck (list): list of all cards in the deck
    """
    
    def __init__(self, players):
        """Initialize the Game with players, create and shuffle the deck,
        and deal cards.

        Args:
            players (list): list of Player objects participating in the game
            
        Side Effects:
            Creates a TurnManager object
                Initializes and shuffles a Deck object
                Deals cards to all players  
        """
        self.players = players
        self.turn_manager = TurnManager()
        deck = Deck()
        self.deck = deck.cards
        self.current_rank_index = 0
        self.deal_cards()

    def deal_cards(self):
        """Deal cards evenly to all players.
        
        Side Effects:
            Distributes cards from the deck to each player's hand
        """
        p = 0
        while self.deck:
            card = self.deck.pop()
            self.players[p].deck.append(card)
            p = (p+1) % len(self.players)

        for pl in self.players:
            print(f"{pl.name} received {len(pl.deck)} cards.")

    def get_required_rank(self):
        """Get the current required rank for the turn.
=
        Returns:
            str: the required rank for the current turn
        """
        return RANKS[self.current_rank_index]

    def advance_rank(self):
        """Advance to the next required rank for the turn.
        
        Side Effects:
            Updates the current_rank_index to the next rank in RANKS
            """
            
        self.current_rank_index = (self.current_rank_index + 1) % len(RANKS)

    def play(self):
        
        """Start and manage the game play until a player wins.
        
        Side Effects:
            Prints the current turn, required rank, and player actions.

        Returns:
            str: name of the winning player
        """
        
        turn = 0
        round_number = 1
        
        print(f"\n\n>>>>>>>>>>>>>>>>>>>>> ROUND {round_number} <<<<<<<<<<<<<<<<<<<<<\n")
        
        while True:
            required_rank = self.get_required_rank()
            player = self.players[turn]
            
            print("\n" + "-"*50)
            print(f"TURN: {player.name} — Required Rank: {required_rank}")

            if not player.has_cards():
                print(f"{player.name} has no cards — SKIPPING turn.")
                turn = (turn + 1) % len(self.players)
                self.advance_rank()
                continue 
                
                
            played_cards, claim = player.take_turn(required_rank)
            self.turn_manager.add_play(played_cards)

            emptied_hand = not player.has_cards()

            caller = None
            for i in range(1, len(self.players)):
                other = self.players[(turn+i) % len(self.players)]
                if isinstance(other, HumanPlayer):
                    print("\nYour hand:")
                    sorted_hand = sorted(range(len(other.deck)), key=lambda i: RANKS.index(other.deck[i]))
                    for display_i, real_i in enumerate(sorted_hand):
                        print(f"{other.deck[real_i]}", end='  ')
                    print("\n")
                    resp = input(f"{other.name}, call BS on {player.name}? (Y/N): ").strip().upper()
                    if resp == "Y":
                        caller = other
                        break
                else:
                    if other.decide_call_bluff(player, claim, len(played_cards)):
                        caller = other
                        break

            if caller:
                picker = self.turn_manager.resolve_bluff(caller, player, played_cards, claim)
                if picker is player and emptied_hand:
                    print(f"{player.name} emptied hand but was caught — no win.")
            else:
                print("No BS call — cards stay on pile.")
                if emptied_hand:
                    print(f"\n{player.name} WINS — no cards left and no BS call!")
                    return player.name

            for p in self.players:
                if len(p.deck) == 0:
                    print(f"\n{p.name} wins!")
                    return p.name
            
            turn = (turn + 1) % len(self.players)
            self.advance_rank()

            new_rank = self.get_required_rank()
            if new_rank == "Ace":
                round_number += 1 
                print(f"\n\n>>>>>>>>>> ROUND {round_number} <<<<<<<<<<\n")

# Menu (4C: Max 1 human + 3 CPUs)
def main():
    """starts the game (main menu of game).
    prints the game title and gives a summary of the rules
    asks the user for their name, and if left blank it defaults to "Human"
    asks how many CPU players to include (2-6)
    creates the human player and the chosen number of CPU players
    sets up the Game object, which deals cards and runs the game
    optionally processes command line arguments using argparse (--name and --cpus) 
    
    Side effects:
        prints text to the console
        reads user input for name and CPU count
        creates player objects and starts the game setup 
    """
    parser = argparse.ArgumentParser(description="Play BS card game.")
    parser.add_argument("--name", type=str, help="Name of the human player.")
    parser.add_argument("--cpus", type=int, help="Number of CPU players (2-6).")
    
    args = parser.parse_args()
    
    print("BS a.k.a I Doubt It Card Game — Up to 1 Human and 6 CPUs\n")
    print("Rules Summary:")

    print("""
          - Players take turns playing 1 to 4 cards face down, claiming them as a specific rank.
          - The required rank cycles through Ace to King.
          - Other players may call "BS" if they suspect a bluff.
          - If a bluff is called, and  the accused lied, they pick up the pile. 
          - If a bluff is called, and the accused is truthful, the accuser picks up the pile.
          - First player to get rid of all their cards wins!\n
          """)
    
    if args.name:
        name = args.name
    else:
        name = input("Enter your name: ").strip() or "Human"
    
    human = HumanPlayer(name)

    if args.cpus is not None:
        num_cpu = args.cpus
        if not (2 <= num_cpu <= 6):
            print("CPU count must be between 2 and 6.")
            return 
    else:
        while True:
            try:
                num_cpu = int(input("How many CPU players? (2–6): "))
                if 2 <= num_cpu <= 6:
                    break
            except:
                pass
            print("Invalid number.")

    players = [human] + [CpuPlayer(f"CPU{i+1}") for i in range(num_cpu)]

    game = Game(players)
    winner = game.play()
    print(f"\nGAME OVER — Winner: {winner}")

if __name__ == "__main__":
    main()
