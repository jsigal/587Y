"""
Rock, Paper, Scissors, Lizard, Spock Game
Object-oriented implementation supporting 1-4 players with multiple rounds and score tracking.
"""

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict
from abc import ABC, abstractmethod


class MoveType(Enum):
    """Enumeration of all valid moves in RPSLS."""
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    LIZARD = "lizard"
    SPOCK = "spock"


class Move:
    """Represents a move in RPSLS with its defeat relationships."""
    
    # Define defeat relationships: move_type -> [moves it defeats]
    DEFEATS = {
        MoveType.ROCK: [MoveType.SCISSORS, MoveType.LIZARD],
        MoveType.PAPER: [MoveType.ROCK, MoveType.SPOCK],
        MoveType.SCISSORS: [MoveType.PAPER, MoveType.LIZARD],
        MoveType.LIZARD: [MoveType.SPOCK, MoveType.PAPER],
        MoveType.SPOCK: [MoveType.SCISSORS, MoveType.ROCK],
    }
    
    # Abbreviation mappings
    ABBREVIATIONS = {
        "r": MoveType.ROCK,
        "p": MoveType.PAPER,
        "s": MoveType.SCISSORS,
        "l": MoveType.LIZARD,
        "sp": MoveType.SPOCK,
    }
    
    def __init__(self, move_type: MoveType):
        self.move_type = move_type
        self.name = move_type.value
    
    def defeats(self, other: 'Move') -> bool:
        """Check if this move defeats another move."""
        return other.move_type in self.DEFEATS[self.move_type]
    
    def __str__(self) -> str:
        return self.name.capitalize()
    
    def __repr__(self) -> str:
        return f"Move({self.move_type.name})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Move):
            return NotImplemented
        return self.move_type == other.move_type
    
    def __hash__(self) -> int:
        return hash(self.move_type)
    
    @classmethod
    def from_string(cls, choice: str) -> Optional['Move']:
        """Create a Move instance from a string choice."""
        choice_lower = choice.lower().strip()
        
        # Try full name first
        try:
            move_type = MoveType(choice_lower)
            return cls(move_type)
        except ValueError:
            pass
        
        # Try abbreviation
        move_type = cls.ABBREVIATIONS.get(choice_lower)
        if move_type:
            return cls(move_type)
        
        return None
    
    @classmethod
    def all_moves(cls) -> List['Move']:
        """Get a list of all possible moves."""
        return [cls(move_type) for move_type in MoveType]
    
    @classmethod
    def random(cls) -> 'Move':
        """Get a random move."""
        return cls(random.choice(list(MoveType)))


class PlayerStrategy(ABC):
    """Strategy pattern for different player types."""
    
    @abstractmethod
    def get_move(self, player_name: str) -> Move:
        """Get a move from the player."""
        pass


class HumanStrategy(PlayerStrategy):
    """Strategy for human players."""
    
    def get_move(self, player_name: str) -> Move:
        """Prompt human player for their move."""
        print(f"\n{player_name}'s turn!")
        print("Available moves: Rock (r), Paper (p), Scissors (s), Lizard (l), Spock (sp)")
        while True:
            choice = input(f"{player_name}, enter your move: ").strip()
            move = Move.from_string(choice)
            if move:
                return move
            print("Invalid move! Please try again.")


class ComputerStrategy(PlayerStrategy):
    """Strategy for computer players."""
    
    def get_move(self, player_name: str) -> Move:
        """Generate a random move for computer player."""
        move = Move.random()
        print(f"{player_name} chooses: {move}")
        return move


@dataclass
class Player:
    """Represents a player in the game."""
    
    name: str
    strategy: PlayerStrategy
    wins: int = field(default=0, init=False)
    
    def choose_move(self) -> Move:
        """Get the player's move choice using their strategy."""
        return self.strategy.get_move(self.name)
    
    def add_win(self) -> None:
        """Increment the player's win count."""
        self.wins += 1
    
    def __str__(self) -> str:
        return f"{self.name} (Wins: {self.wins})"
    
    def __hash__(self) -> int:
        """Make Player hashable by using name as hash."""
        return hash(self.name)
    
    def __eq__(self, other) -> bool:
        """Compare players by name."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name
    
    @classmethod
    def human(cls, name: str) -> 'Player':
        """Create a human player."""
        return cls(name, HumanStrategy())
    
    @classmethod
    def computer(cls, name: str = "Computer") -> 'Player':
        """Create a computer player."""
        return cls(name, ComputerStrategy())


class Game:
    """Main game class managing rounds, players, and scoring."""
    
    RULES = [
        "Scissors cuts Paper",
        "Paper covers Rock",
        "Rock crushes Lizard",
        "Lizard poisons Spock",
        "Spock smashes Scissors",
        "Scissors decapitates Lizard",
        "Lizard eats Paper",
        "Paper disproves Spock",
        "Spock vaporizes Rock",
        "Rock crushes Scissors",
    ]
    
    MIN_PLAYERS = 1
    MAX_PLAYERS = 4
    
    def __init__(self, num_players: int):
        """Initialize the game with specified number of players."""
        if not self.MIN_PLAYERS <= num_players <= self.MAX_PLAYERS:
            raise ValueError(f"Number of players must be between {self.MIN_PLAYERS} and {self.MAX_PLAYERS}")
        
        self.players: List[Player] = self._create_players(num_players)
        self.round_number = 0
    
    def _create_players(self, num_players: int) -> List[Player]:
        """Create the list of players."""
        players = []
        for i in range(1, num_players + 1):
            name = input(f"Enter name for Player {i}: ").strip() or f"Player {i}"
            players.append(Player.human(name))
        
        # If only one player, add computer player
        if num_players == 1:
            players.append(Player.computer())
        
        return players
    
    @property
    def total_rounds(self) -> int:
        """Total number of rounds played."""
        return self.round_number
    
    def play_round(self) -> None:
        """Play a single round of RPSLS."""
        self.round_number += 1
        
        print(f"\n{'='*60}")
        print(f"Round {self.round_number}")
        print(f"{'='*60}")
        
        # Get moves from all players using dictionary comprehension
        moves = {player: player.choose_move() for player in self.players}
        
        # Determine winners
        winners = self._determine_winners(moves)
        
        # Display results
        self._display_round_results(moves, winners)
        
        # Award wins to winners
        for winner in winners:
            winner.add_win()
        
        # Display current standings
        self._display_standings()
    
    def _determine_winners(self, moves: Dict[Player, Move]) -> List[Player]:
        """Determine the winner(s) of a round."""
        players_list = list(moves.keys())
        
        # Check if all players have the same move (universal tie)
        if len(set(moves.values())) == 1:
            return []
        
        # Find players whose move beats all other moves
        winners = [
            player for player in players_list
            if all(
                player == other or moves[player].defeats(moves[other])
                for other in players_list
            )
        ]
        
        return winners
    
    def _display_round_results(self, moves: Dict[Player, Move], winners: List[Player]) -> None:
        """Display the results of a round."""
        print(f"\n{'='*60}")
        print("Round Results:")
        print(f"{'='*60}")
        
        for player, move in moves.items():
            print(f"{player.name}: {move}")
        
        if not winners:
            print("\nIt's a tie! No winners this round.")
        elif len(winners) == 1:
            print(f"\n{winners[0].name} wins this round!")
        else:
            winner_names = ", ".join(w.name for w in winners)
            print(f"\nTie! Winners: {winner_names}")
    
    def _display_standings(self) -> None:
        """Display current game standings."""
        print(f"\n{'='*60}")
        print("Current Standings:")
        print(f"{'='*60}")
        
        sorted_players = sorted(self.players, key=lambda p: p.wins, reverse=True)
        for player in sorted_players:
            print(f"{player.name}: {player.wins} win(s)")
        
        print(f"{'='*60}\n")
    
    def play(self) -> None:
        """Main game loop."""
        self._display_welcome()
        
        while True:
            self.play_round()
            
            if not self._should_continue():
                break
        
        self._display_final_results()
    
    def _display_welcome(self) -> None:
        """Display welcome message and rules."""
        print("\n" + "="*60)
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("="*60)
        print("\nRules:")
        for rule in self.RULES:
            print(f"  - {rule}")
        print("="*60)
    
    def _should_continue(self) -> bool:
        """Ask if players want to continue playing."""
        response = input("Play another round? (yes/no): ").strip().lower()
        return response in ("yes", "y")
    
    def _display_final_results(self) -> None:
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
        
        # Determine overall winner(s)
        if sorted_players:
            max_wins = sorted_players[0].wins
            overall_winners = [p for p in sorted_players if p.wins == max_wins]
            
            if len(overall_winners) == 1:
                print(f"\n🏆 Overall Winner: {overall_winners[0].name}! 🏆")
            elif max_wins > 0:
                winner_names = ", ".join(w.name for w in overall_winners)
                print(f"\n🏆 Overall Winners (Tie): {winner_names}! 🏆")
            else:
                print("\nNo overall winner (all players tied).")
        
        print("="*60)
        print("\nThanks for playing Rock, Paper, Scissors, Lizard, Spock!")


def get_num_players() -> int:
    """Get the number of players from user input."""
    print("="*60)
    print("Rock, Paper, Scissors, Lizard, Spock")
    print("="*60)
    print(f"\nHow many players? ({Game.MIN_PLAYERS}-{Game.MAX_PLAYERS})")
    print("Note: If 1 player, the computer will play as the second player.")
    
    while True:
        try:
            num_players = int(input("Enter number of players: ").strip())
            if Game.MIN_PLAYERS <= num_players <= Game.MAX_PLAYERS:
                return num_players
            print(f"Please enter a number between {Game.MIN_PLAYERS} and {Game.MAX_PLAYERS}.")
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    """Main entry point for the game."""
    num_players = get_num_players()
    game = Game(num_players)
    game.play()


if __name__ == "__main__":
    main()
