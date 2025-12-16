"""
Rock, Paper, Scissors, Lizard, Spock Game
Object-oriented implementation supporting 1-4 players with multiple rounds and score tracking.
"""

import random
from typing import List, Optional, Dict
from abc import ABC, abstractmethod


class Move(ABC):
    """Base class for all moves in RPSLS."""
    
    def __init__(self, name: str):
        self.name = name
        self.beats: List[str] = []
    
    def defeats(self, other: 'Move') -> bool:
        """Check if this move defeats another move."""
        return other.name in self.beats
    
    def __str__(self) -> str:
        return self.name.capitalize()
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Move):
            return False
        return self.name == other.name


class Rock(Move):
    """Rock move - crushes Scissors and Lizard."""
    
    def __init__(self):
        super().__init__("rock")
        self.beats = ["scissors", "lizard"]


class Paper(Move):
    """Paper move - covers Rock and disproves Spock."""
    
    def __init__(self):
        super().__init__("paper")
        self.beats = ["rock", "spock"]


class Scissors(Move):
    """Scissors move - cuts Paper and decapitates Lizard."""
    
    def __init__(self):
        super().__init__("scissors")
        self.beats = ["paper", "lizard"]


class Lizard(Move):
    """Lizard move - poisons Spock and eats Paper."""
    
    def __init__(self):
        super().__init__("lizard")
        self.beats = ["spock", "paper"]


class Spock(Move):
    """Spock move - smashes Scissors and vaporizes Rock."""
    
    def __init__(self):
        super().__init__("spock")
        self.beats = ["scissors", "rock"]


class MoveFactory:
    """Factory class to create move instances."""
    
    MOVES = {
        "rock": Rock,
        "paper": Paper,
        "scissors": Scissors,
        "lizard": Lizard,
        "spock": Spock,
        "r": Rock,
        "p": Paper,
        "s": Scissors,
        "l": Lizard,
        "sp": Spock,
    }
    
    @classmethod
    def create(cls, choice: str) -> Optional[Move]:
        """Create a move from a string choice."""
        choice_lower = choice.lower().strip()
        move_class = cls.MOVES.get(choice_lower)
        if move_class:
            return move_class()
        return None
    
    @classmethod
    def get_all_moves(cls) -> List[str]:
        """Get list of all valid move names."""
        return ["rock", "paper", "scissors", "lizard", "spock"]
    
    @classmethod
    def get_random_move(cls) -> Move:
        """Get a random move."""
        move_name = random.choice(cls.get_all_moves())
        return cls.create(move_name)


class Player:
    """Represents a player in the game."""
    
    def __init__(self, name: str, is_computer: bool = False):
        self.name = name
        self.is_computer = is_computer
        self.wins = 0
    
    def choose_move(self) -> Optional[Move]:
        """Get the player's move choice."""
        if self.is_computer:
            move = MoveFactory.get_random_move()
            print(f"{self.name} chooses: {move}")
            return move
        else:
            print(f"\n{self.name}'s turn!")
            print("Available moves: Rock (r), Paper (p), Scissors (s), Lizard (l), Spock (sp)")
            while True:
                choice = input(f"{self.name}, enter your move: ").strip()
                move = MoveFactory.create(choice)
                if move:
                    return move
                print("Invalid move! Please try again.")
    
    def add_win(self):
        """Increment the player's win count."""
        self.wins += 1
    
    def __str__(self) -> str:
        return f"{self.name} (Wins: {self.wins})"


class Game:
    """Main game class managing rounds, players, and scoring."""
    
    def __init__(self, num_players: int):
        """Initialize the game with specified number of players."""
        if not 1 <= num_players <= 4:
            raise ValueError("Number of players must be between 1 and 4")
        
        self.players: List[Player] = []
        self.round_number = 0
        self.total_rounds = 0
        
        # Create human players
        for i in range(1, num_players + 1):
            name = input(f"Enter name for Player {i}: ").strip() or f"Player {i}"
            self.players.append(Player(name, is_computer=False))
        
        # If only one player, add computer player
        if num_players == 1:
            self.players.append(Player("Computer", is_computer=True))
    
    def play_round(self) -> None:
        """Play a single round of RPSLS."""
        self.round_number += 1
        self.total_rounds += 1
        
        print(f"\n{'='*60}")
        print(f"Round {self.round_number}")
        print(f"{'='*60}")
        
        # Get moves from all players
        moves: Dict[Player, Move] = {}
        for player in self.players:
            move = player.choose_move()
            moves[player] = move
        
        # Determine winners
        winners = self.determine_winners(moves)
        
        # Display results
        print(f"\n{'='*60}")
        print("Round Results:")
        print(f"{'='*60}")
        
        for player, move in moves.items():
            print(f"{player.name}: {move}")
        
        if len(winners) == 0:
            print("\nIt's a tie! No winners this round.")
        elif len(winners) == 1:
            winner = winners[0]
            winner.add_win()
            print(f"\n{winner.name} wins this round!")
        else:
            # Multiple winners (tie between some players)
            winner_names = [w.name for w in winners]
            print(f"\nTie! Winners: {', '.join(winner_names)}")
            for winner in winners:
                winner.add_win()
        
        # Display current standings
        self.display_standings()
    
    def determine_winners(self, moves: Dict[Player, Move]) -> List[Player]:
        """Determine the winner(s) of a round."""
        players_list = list(moves.keys())
        
        # Check if all players have the same move (tie)
        all_same = all(moves[p] == moves[players_list[0]] for p in players_list)
        if all_same:
            return []  # Everyone tied
        
        winners = []
        
        # Find players whose move beats all other players' moves
        for player in players_list:
            move = moves[player]
            beats_all = True
            
            # Check if this move beats all other moves
            for other_player in players_list:
                if player != other_player:
                    other_move = moves[other_player]
                    # If moves are the same, continue (handled above)
                    if move == other_move:
                        continue
                    # If this move doesn't beat the other move, it's not a winner
                    if not move.defeats(other_move):
                        beats_all = False
                        break
            
            if beats_all:
                winners.append(player)
        
        # If we found winners, return them
        if winners:
            return winners
        
        # If no clear winner (no one beats everyone), return empty list (tie)
        return []
    
    def display_standings(self) -> None:
        """Display current game standings."""
        print(f"\n{'='*60}")
        print("Current Standings:")
        print(f"{'='*60}")
        for player in sorted(self.players, key=lambda p: p.wins, reverse=True):
            print(f"{player.name}: {player.wins} win(s)")
        print(f"{'='*60}\n")
    
    def play(self) -> None:
        """Main game loop."""
        print("\n" + "="*60)
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("="*60)
        print("\nRules:")
        print("  - Scissors cuts Paper")
        print("  - Paper covers Rock")
        print("  - Rock crushes Lizard")
        print("  - Lizard poisons Spock")
        print("  - Spock smashes Scissors")
        print("  - Scissors decapitates Lizard")
        print("  - Lizard eats Paper")
        print("  - Paper disproves Spock")
        print("  - Spock vaporizes Rock")
        print("  - Rock crushes Scissors")
        print("="*60)
        
        while True:
            self.play_round()
            
            # Ask if players want to continue
            print("Play another round? (yes/no): ", end="")
            continue_game = input().strip().lower()
            if continue_game not in ["yes", "y"]:
                break
        
        # Display final results
        self.display_final_results()
    
    def display_final_results(self) -> None:
        """Display final game results."""
        print("\n" + "="*60)
        print("FINAL GAME RESULTS")
        print("="*60)
        print(f"Total rounds played: {self.total_rounds}\n")
        
        # Sort players by wins
        sorted_players = sorted(self.players, key=lambda p: p.wins, reverse=True)
        
        print("Final Standings:")
        print("-" * 60)
        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player.name}: {player.wins} win(s)")
        
        # Check for overall winner(s)
        max_wins = sorted_players[0].wins
        overall_winners = [p for p in sorted_players if p.wins == max_wins]
        
        if len(overall_winners) == 1:
            print(f"\n🏆 Overall Winner: {overall_winners[0].name}! 🏆")
        elif max_wins > 0:
            winner_names = [w.name for w in overall_winners]
            print(f"\n🏆 Overall Winners (Tie): {', '.join(winner_names)}! 🏆")
        else:
            print("\nNo overall winner (all players tied).")
        
        print("="*60)
        print("\nThanks for playing Rock, Paper, Scissors, Lizard, Spock!")


def main():
    """Main entry point for the game."""
    print("="*60)
    print("Rock, Paper, Scissors, Lizard, Spock")
    print("="*60)
    print("\nHow many players? (1-4)")
    print("Note: If 1 player, the computer will play as the second player.")
    
    while True:
        try:
            num_players = int(input("Enter number of players: ").strip())
            if 1 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Create and play the game
    game = Game(num_players)
    game.play()


if __name__ == "__main__":
    main()

