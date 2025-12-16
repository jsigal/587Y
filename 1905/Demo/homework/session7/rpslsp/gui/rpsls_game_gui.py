"""
Rock, Paper, Scissors, Lizard, Spock Game - GUI Version
Graphical user interface implementation using tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Optional
from rpsls_game import Move, MoveType, Player, PlayerStrategy, ComputerStrategy, Game


class GUIHumanStrategy(PlayerStrategy):
    """Strategy for human players in GUI - waits for button click."""
    
    def __init__(self):
        self.selected_move: Optional[Move] = None
    
    def get_move(self, player_name: str) -> Move:
        """This will be called after the GUI sets selected_move."""
        return self.selected_move


class RPSLSGameGUI:
    """Graphical user interface for Rock, Paper, Scissors, Lizard, Spock game."""
    
    MOVE_COLORS = {
        MoveType.ROCK: "#8B7355",      # Brown
        MoveType.PAPER: "#F5F5DC",     # Beige
        MoveType.SCISSORS: "#C0C0C0",  # Silver
        MoveType.LIZARD: "#90EE90",    # Light Green
        MoveType.SPOCK: "#4B0082",     # Indigo
    }
    
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors, Lizard, Spock")
        self.root.geometry("900x700")
        self.root.configure(bg='#2C3E50')  # Dark blue-gray background
        
        # Game state
        self.game: Optional[Game] = None
        self.current_player_index = 0
        self.player_moves: Dict[Player, Move] = {}
        self.waiting_for_move = False
        
        # Create startup screen
        self.create_startup_screen()
    
    def create_startup_screen(self):
        """Create the initial setup screen for player selection."""
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Rock, Paper, Scissors, Lizard, Spock",
            font=('Arial', 24, 'bold'),
            bg='#2C3E50',
            fg='white'
        )
        title_label.pack(pady=30)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Select number of players (1-4)\nIf 1 player, computer will play as opponent",
            font=('Arial', 12),
            bg='#2C3E50',
            fg='#BDC3C7',
            justify=tk.CENTER
        )
        instructions.pack(pady=20)
        
        # Player selection frame
        player_frame = tk.Frame(self.root, bg='#2C3E50')
        player_frame.pack(pady=20)
        
        # Number of players selection
        num_label = tk.Label(
            player_frame,
            text="Number of Players:",
            font=('Arial', 14),
            bg='#2C3E50',
            fg='white'
        )
        num_label.pack(side=tk.LEFT, padx=10)
        
        self.num_players_var = tk.IntVar(value=1)
        num_spinbox = tk.Spinbox(
            player_frame,
            from_=1,
            to=4,
            textvariable=self.num_players_var,
            font=('Arial', 12),
            width=5
        )
        num_spinbox.pack(side=tk.LEFT, padx=10)
        
        # Player name entries
        self.name_vars: List[tk.StringVar] = []
        self.name_entries: List[tk.Entry] = []
        name_frame = tk.Frame(self.root, bg='#2C3E50')
        name_frame.pack(pady=20)
        
        def update_name_entries(*args):
            """Update the number of name entry fields."""
            # Clear existing entries
            for entry in self.name_entries:
                entry.destroy()
            self.name_entries.clear()
            self.name_vars.clear()
            
            # Create new entries
            num_players = self.num_players_var.get()
            for i in range(num_players):
                var = tk.StringVar(value=f"Player {i+1}")
                label = tk.Label(
                    name_frame,
                    text=f"Player {i+1}:",
                    font=('Arial', 11),
                    bg='#2C3E50',
                    fg='white'
                )
                label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.E)
                
                entry = tk.Entry(
                    name_frame,
                    textvariable=var,
                    font=('Arial', 11),
                    width=20
                )
                entry.grid(row=i, column=1, padx=5, pady=5)
                
                self.name_vars.append(var)
                self.name_entries.append(entry)
        
        self.num_players_var.trace('w', update_name_entries)
        update_name_entries()  # Initial call
        
        # Start button
        start_button = tk.Button(
            self.root,
            text="Start Game",
            command=self.start_game,
            font=('Arial', 14, 'bold'),
            bg='#27AE60',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        start_button.pack(pady=30)
        
        # Rules display
        rules_frame = tk.Frame(self.root, bg='#34495E', relief=tk.RIDGE, borderwidth=2)
        rules_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        rules_title = tk.Label(
            rules_frame,
            text="Rules:",
            font=('Arial', 14, 'bold'),
            bg='#34495E',
            fg='white'
        )
        rules_title.pack(pady=10)
        
        rules_text = "\n".join([f"• {rule}" for rule in Game.RULES])
        rules_label = tk.Label(
            rules_frame,
            text=rules_text,
            font=('Arial', 10),
            bg='#34495E',
            fg='#ECF0F1',
            justify=tk.LEFT
        )
        rules_label.pack(pady=10, padx=10)
    
    def start_game(self):
        """Initialize and start the game."""
        num_players = self.num_players_var.get()
        
        # Get player names
        player_names = [var.get().strip() or f"Player {i+1}" 
                       for i, var in enumerate(self.name_vars)]
        
        # Initialize game
        try:
            self.game = Game.__new__(Game)
            self.game.players = []
            self.game.round_number = 0
            
            # Create human players with GUI strategy
            for name in player_names:
                strategy = GUIHumanStrategy()
                player = Player(name, strategy)
                self.game.players.append(player)
            
            # Add computer player if only 1 human player
            if num_players == 1:
                computer_player = Player("Computer", ComputerStrategy())
                self.game.players.append(computer_player)
            
            # Clear startup and show game screen
            self.create_game_screen()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start game: {e}")
    
    def create_game_screen(self):
        """Create the main game screen."""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Rock, Paper, Scissors, Lizard, Spock",
            font=('Arial', 20, 'bold'),
            bg='#2C3E50',
            fg='white'
        )
        title_label.pack(pady=10)
        
        # Game info frame
        info_frame = tk.Frame(self.root, bg='#34495E', relief=tk.RIDGE, borderwidth=2)
        info_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.round_label = tk.Label(
            info_frame,
            text="Round 0",
            font=('Arial', 14, 'bold'),
            bg='#34495E',
            fg='#F39C12'
        )
        self.round_label.pack(pady=5)
        
        self.status_label = tk.Label(
            info_frame,
            text="Ready to play!",
            font=('Arial', 12),
            bg='#34495E',
            fg='white'
        )
        self.status_label.pack(pady=5)
        
        # Scoreboard frame
        score_frame = tk.Frame(self.root, bg='#2C3E50')
        score_frame.pack(pady=10)
        
        score_title = tk.Label(
            score_frame,
            text="Scoreboard",
            font=('Arial', 14, 'bold'),
            bg='#2C3E50',
            fg='white'
        )
        score_title.pack()
        
        self.score_labels: Dict[Player, tk.Label] = {}
        for player in self.game.players:
            score_label = tk.Label(
                score_frame,
                text=f"{player.name}: 0 wins",
                font=('Arial', 11),
                bg='#2C3E50',
                fg='#ECF0F1'
            )
            score_label.pack(pady=2)
            self.score_labels[player] = score_label
        
        # Moves selection frame
        moves_frame = tk.Frame(self.root, bg='#2C3E50')
        moves_frame.pack(pady=20)
        
        moves_title = tk.Label(
            moves_frame,
            text="Select Your Move:",
            font=('Arial', 14, 'bold'),
            bg='#2C3E50',
            fg='white'
        )
        moves_title.pack(pady=10)
        
        # Move buttons
        self.move_buttons: Dict[MoveType, tk.Button] = {}
        moves_grid = tk.Frame(moves_frame, bg='#2C3E50')
        moves_grid.pack()
        
        move_names = {
            MoveType.ROCK: "Rock",
            MoveType.PAPER: "Paper",
            MoveType.SCISSORS: "Scissors",
            MoveType.LIZARD: "Lizard",
            MoveType.SPOCK: "Spock"
        }
        
        for move_type in MoveType:
            button = tk.Button(
                moves_grid,
                text=move_names[move_type],
                command=lambda mt=move_type: self.select_move(mt),
                font=('Arial', 12, 'bold'),
                bg=self.MOVE_COLORS[move_type],
                fg='white',
                width=12,
                height=2,
                cursor='hand2',
                relief=tk.RAISED,
                borderwidth=3
            )
            button.grid(row=0, column=list(MoveType).index(move_type), padx=5, pady=5)
            self.move_buttons[move_type] = button
        
        # Results display area
        self.results_text = tk.Text(
            self.root,
            height=10,
            width=80,
            font=('Arial', 10),
            bg='#34495E',
            fg='white',
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.results_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg='#2C3E50')
        control_frame.pack(pady=10)
        
        self.play_button = tk.Button(
            control_frame,
            text="Play Round",
            command=self.play_round,
            font=('Arial', 12, 'bold'),
            bg='#27AE60',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.play_button.pack(side=tk.LEFT, padx=10)
        
        self.new_game_button = tk.Button(
            control_frame,
            text="New Game",
            command=self.reset_game,
            font=('Arial', 12, 'bold'),
            bg='#3498DB',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.new_game_button.pack(side=tk.LEFT, padx=10)
        
        # Start first round
        self.reset_round_state()
        self.update_status("Click 'Play Round' to start!")
    
    def reset_round_state(self):
        """Reset state for a new round."""
        self.player_moves.clear()
        self.current_player_index = 0
        self.waiting_for_move = False
        
        # Enable all move buttons
        for button in self.move_buttons.values():
            button.config(state=tk.NORMAL)
        
        # Clear results
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)
    
    def select_move(self, move_type: MoveType):
        """Handle move selection from button click."""
        if not self.waiting_for_move:
            return
        
        move = Move(move_type)
        current_player = self.game.players[self.current_player_index]
        
        # Store the move for human players
        if hasattr(current_player.strategy, 'selected_move'):
            current_player.strategy.selected_move = move
            self.player_moves[current_player] = move
            self.log_message(f"{current_player.name} selected: {move}")
            
            # Move to next player
            self.current_player_index += 1
            if self.current_player_index >= len(self.game.players):
                self.waiting_for_move = False
                self.process_round()
            else:
                self.get_next_player_move()
        else:
            messagebox.showwarning("Warning", "Not your turn yet!")
    
    def get_next_player_move(self):
        """Get the move from the next player."""
        if self.current_player_index >= len(self.game.players):
            return
        
        player = self.game.players[self.current_player_index]
        
        # If computer player, get move immediately
        if isinstance(player.strategy, ComputerStrategy):
            # Use root.after to add a small delay for better UX
            self.root.after(500, lambda: self.process_computer_move(player))
        else:
            # Human player - wait for button click
            self.waiting_for_move = True
            self.update_status(f"{player.name}'s turn - Select your move!")
    
    def process_computer_move(self, player: Player):
        """Process a computer player's move."""
        move = player.choose_move()
        self.player_moves[player] = move
        self.log_message(f"{player.name} chose: {move}")
        self.current_player_index += 1
        
        if self.current_player_index >= len(self.game.players):
            self.waiting_for_move = False
            self.process_round()
        else:
            self.get_next_player_move()
    
    def play_round(self):
        """Start a new round."""
        if self.game.round_number > 0 and not self.player_moves:
            messagebox.showinfo("Info", "Please wait for the current round to complete.")
            return
        
        self.game.round_number += 1
        self.update_round_label()
        self.reset_round_state()
        
        self.log_message(f"\n{'='*60}")
        self.log_message(f"Round {self.game.round_number}")
        self.log_message(f"{'='*60}")
        
        # Disable play button during round
        self.play_button.config(state=tk.DISABLED)
        
        # Start getting moves
        self.get_next_player_move()
    
    def process_round(self):
        """Process the round after all moves are collected."""
        # Determine winners
        winners = self.game._determine_winners(self.player_moves)
        
        # Display results
        self.log_message("\nRound Results:")
        for player, move in self.player_moves.items():
            self.log_message(f"{player.name}: {move}")
        
        # Award wins
        if not winners:
            self.log_message("\nIt's a tie! No winners this round.")
            self.update_status("Round tied! No winners.")
        elif len(winners) == 1:
            winners[0].add_win()
            self.log_message(f"\n🏆 {winners[0].name} wins this round! 🏆")
            self.update_status(f"{winners[0].name} wins!")
        else:
            winner_names = ", ".join(w.name for w in winners)
            self.log_message(f"\n🏆 Tie! Winners: {winner_names} 🏆")
            for winner in winners:
                winner.add_win()
            self.update_status(f"Multiple winners: {winner_names}")
        
        # Update scoreboard
        self.update_scoreboard()
        
        # Re-enable play button
        self.play_button.config(state=tk.NORMAL)
    
    def update_round_label(self):
        """Update the round number display."""
        self.round_label.config(text=f"Round {self.game.round_number}")
    
    def update_status(self, message: str):
        """Update the status label."""
        self.status_label.config(text=message)
    
    def update_scoreboard(self):
        """Update the scoreboard display."""
        sorted_players = sorted(self.game.players, key=lambda p: p.wins, reverse=True)
        for player, label in self.score_labels.items():
            rank = sorted_players.index(player) + 1
            label.config(
                text=f"{rank}. {player.name}: {player.wins} win(s)",
                fg='#F39C12' if player.wins > 0 and player == sorted_players[0] else '#ECF0F1',
                font=('Arial', 11, 'bold' if player == sorted_players[0] else 'normal')
            )
    
    def log_message(self, message: str):
        """Add a message to the results text area."""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.insert(tk.END, message + "\n")
        self.results_text.see(tk.END)
        self.results_text.config(state=tk.DISABLED)
    
    def reset_game(self):
        """Reset the game and return to startup screen."""
        if messagebox.askyesno("New Game", "Are you sure you want to start a new game?"):
            self.create_startup_screen()


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = RPSLSGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

