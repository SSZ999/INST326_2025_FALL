
import random

# Constants
RANKS = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
COPIES_PER_RANK = 4
MAX_PLAY = 4   # max cards per turn for both CPU & human

# Deck class
class Deck:
    """Deck of 52 cards represented by ranks only."""
    def __init__(self):
        self.cards = RANKS * COPIES_PER_RANK
        random.shuffle(self.cards)

# Player base class
class Player:
    """Base class for human & CPU players."""
    def __init__(self, name):
        self.name = name
        self.deck = []

    def __repr__(self):
        return f"<Player {self.name} ({len(self.deck)} cards)>"

    def has_cards(self):
        return len(self.deck) > 0

    def remove_cards_by_indices(self, indices):
        """Remove cards by index (descending order) and return them."""
        selected = []
        for idx in sorted(indices, reverse=True):
            selected.append(self.deck.pop(idx))
        selected.reverse()
        return selected


# Human player class
class HumanPlayer(Player):
    def take_turn(self, required_rank):
        print(f"\n{self.name}'s turn — Required claim rank: {required_rank}")
        print("Your cards:")
        for i, card in enumerate(self.deck):
            print(f"[{i}] {card}", end='  ')
        print("\n")

        while True:
            try:
                n = int(input(f"How many cards do you want to play? (1 to {min(MAX_PLAY, len(self.deck))}): "))
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
                indices = [int(p) for p in parts]
            except:
                print("Indices must be numbers.")
                continue

            if any(i < 0 or i >= len(self.deck) for i in indices):
                print("Index out of range.")
                continue

            break

        actual_cards = self.remove_cards_by_indices(indices)
        print(f"{self.name} placed {len(actual_cards)} cards and CLAIMS they are all {required_rank}.")
        return actual_cards, required_rank

# CPU player class
class CpuPlayer(Player):
    def take_turn(self, required_rank):
        rank_positions = [i for i,c in enumerate(self.deck) if c == required_rank]

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
    def __init__(self):
        self.center_pile = []

    def add_play(self, cards):
        self.center_pile.extend(cards)

    def resolve_bluff(self, accuser, accused, played_cards, claimed_rank):
        lied = any(card != claimed_rank for card in played_cards)
        self.center_pile.extend(played_cards)

        if lied:
            taken = self.center_pile.copy()
            self.center_pile.clear()
            accused.deck.extend(taken)
            print(f"{accused.name} LIED and picks up {len(taken)} cards!")
            return accused
        else:
            taken = self.center_pile.copy()
            self.center_pile.clear()
            accuser.deck.extend(taken)
            print(f"{accuser.name} was WRONG and picks up {len(taken)} cards.")
            return accuser

# Game engine class
class Game:
    def __init__(self, players):
        self.players = players
        self.turn_manager = TurnManager()
        deck = Deck()
        self.deck = deck.cards
        self.current_rank_index = 0
        self.deal_cards()

    def deal_cards(self):
        p = 0
        while self.deck:
            card = self.deck.pop()
            self.players[p].deck.append(card)
            p = (p+1) % len(self.players)

        for pl in self.players:
            print(f"{pl.name} received {len(pl.deck)} cards.")

    def get_required_rank(self):
        return RANKS[self.current_rank_index]

    def advance_rank(self):
        self.current_rank_index = (self.current_rank_index + 1) % len(RANKS)

    def play(self):
        turn = 0
        while True:
            player = self.players[turn]
            required_rank = self.get_required_rank()

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

# Menu (4C: Max 1 human + 3 CPUs)
def main():
    print("BS a.k.a I Doubt It Card Game — Up to 1 Human and 3 CPUs\n")
    print("Rules Summary:")

    print("""
          - Players take turns playing 1 to 4 cards face down, claiming them as a specific rank.
          - The required rank cycles through Ace to King.
          - Other players may call "BS" if they suspect a bluff.
          - If a bluff is called, and  the accused lied, they pick up the pile. 
          - If a bluff is called, and the accused is truthful, the accuser picks up the pile.
          - First player to get rid of all their cards wins!\n
          """)
    name = input("Enter your name: ").strip() or "Human"
    human = HumanPlayer(name)

    while True:
        try:
            num_cpu = int(input("How many CPU players? (1–3): "))
            if 1 <= num_cpu <= 3:
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
