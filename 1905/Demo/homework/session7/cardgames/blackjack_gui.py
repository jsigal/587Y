"""
Blackjack game - GUI Version
Graphical user interface implementation using tkinter.
"""
from __future__ import annotations
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import List, Optional
from blackjack import BlackjackGame, Player, Dealer, BlackjackHand
from cardlib_enum import PlayingCard


class BlackjackGUI:
    """Graphical user interface for Blackjack game."""
    
    CARD_COLORS = {
        'red': '#DC143C',      # Crimson for hearts/diamonds
        'black': '#000000',    # Black for clubs/spades
        'background': '#0D4F0D',  # Dark green table
        'card_bg': '#FFFFFF',  # White card background
        'text': '#000000',
        'highlight': '#FFD700'  # Gold for highlights
    }
    
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("1000x800")
        self.root.configure(bg=self.CARD_COLORS['background'])
        
        # Game state
        self.game: Optional[BlackjackGame] = None
        self.current_player_index = 0
        self.waiting_for_action = False
        self.round_in_progress = False
        
        # Create startup screen
        self.create_startup_screen()
    
    def create_startup_screen(self):
        """Create the initial setup screen."""
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="BLACKJACK",
            font=('Arial', 32, 'bold'),
            bg=self.CARD_COLORS['background'],
            fg='white'
        )
        title_label.pack(pady=30)
        
        # Setup frame
        setup_frame = tk.Frame(self.root, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=3)
        setup_frame.pack(pady=20, padx=50)
        
        # Number of players
        num_frame = tk.Frame(setup_frame, bg='#1A5A1A')
        num_frame.pack(pady=15, padx=20)
        
        num_label = tk.Label(
            num_frame,
            text="Number of Players:",
            font=('Arial', 14),
            bg='#1A5A1A',
            fg='white'
        )
        num_label.pack(side=tk.LEFT, padx=10)
        
        self.num_players_var = tk.IntVar(value=1)
        num_spinbox = tk.Spinbox(
            num_frame,
            from_=1,
            to=4,
            textvariable=self.num_players_var,
            font=('Arial', 12),
            width=5
        )
        num_spinbox.pack(side=tk.LEFT, padx=10)
        
        # Starting chips
        chips_frame = tk.Frame(setup_frame, bg='#1A5A1A')
        chips_frame.pack(pady=15, padx=20)
        
        chips_label = tk.Label(
            chips_frame,
            text="Starting Chips:",
            font=('Arial', 14),
            bg='#1A5A1A',
            fg='white'
        )
        chips_label.pack(side=tk.LEFT, padx=10)
        
        self.starting_chips_var = tk.IntVar(value=1000)
        chips_entry = tk.Entry(
            chips_frame,
            textvariable=self.starting_chips_var,
            font=('Arial', 12),
            width=10
        )
        chips_entry.pack(side=tk.LEFT, padx=10)
        
        # Start button
        start_button = tk.Button(
            setup_frame,
            text="Start Game",
            command=self.start_game,
            font=('Arial', 16, 'bold'),
            bg='#27AE60',
            fg='white',
            padx=30,
            pady=15,
            cursor='hand2',
            relief=tk.RAISED,
            borderwidth=3
        )
        start_button.pack(pady=20)
        
        # Rules display
        rules_frame = tk.Frame(self.root, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
        rules_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        rules_title = tk.Label(
            rules_frame,
            text="Rules:",
            font=('Arial', 16, 'bold'),
            bg='#1A5A1A',
            fg='white'
        )
        rules_title.pack(pady=10)
        
        rules_text = (
            "• Goal: Get as close to 21 as possible without going over\n"
            "• Face cards (J, Q, K) are worth 10\n"
            "• Ace can be 1 or 11 (whichever is better)\n"
            "• Blackjack (Ace + 10-value card) pays 3:2\n"
            "• Dealer must hit until 17 or more\n"
            "• Ties push (bet returned)\n"
            "• Minimum bet: 5 chips"
        )
        rules_label = tk.Label(
            rules_frame,
            text=rules_text,
            font=('Arial', 11),
            bg='#1A5A1A',
            fg='#ECF0F1',
            justify=tk.LEFT
        )
        rules_label.pack(pady=10, padx=20)
    
    def start_game(self):
        """Initialize and start the game."""
        try:
            num_players = self.num_players_var.get()
            starting_chips = self.starting_chips_var.get()
            
            if starting_chips < 5:
                messagebox.showerror("Error", "Starting chips must be at least 5!")
                return
            
            self.game = BlackjackGame(num_players, starting_chips)
            self.current_player_index = 0
            self.round_in_progress = False
            
            # Create game screen
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
            text="BLACKJACK",
            font=('Arial', 24, 'bold'),
            bg=self.CARD_COLORS['background'],
            fg='white'
        )
        title_label.pack(pady=10)
        
        # Game info frame
        info_frame = tk.Frame(self.root, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
        info_frame.pack(pady=5, padx=20, fill=tk.X)
        
        self.round_label = tk.Label(
            info_frame,
            text="Round 0",
            font=('Arial', 14, 'bold'),
            bg='#1A5A1A',
            fg='#F39C12'
        )
        self.round_label.pack(pady=5)
        
        self.status_label = tk.Label(
            info_frame,
            text="Ready to play!",
            font=('Arial', 12),
            bg='#1A5A1A',
            fg='white'
        )
        self.status_label.pack(pady=5)
        
        # Main content frame (scrollable)
        main_frame = tk.Frame(self.root, bg=self.CARD_COLORS['background'])
        main_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Dealer section
        dealer_frame = tk.Frame(main_frame, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
        dealer_frame.pack(pady=10, padx=10, fill=tk.X)
        
        dealer_title = tk.Label(
            dealer_frame,
            text="Dealer",
            font=('Arial', 16, 'bold'),
            bg='#1A5A1A',
            fg='white'
        )
        dealer_title.pack(pady=5)
        
        self.dealer_hand_label = tk.Label(
            dealer_frame,
            text="No cards",
            font=('Arial', 12),
            bg='#1A5A1A',
            fg='white'
        )
        self.dealer_hand_label.pack(pady=5)
        
        self.dealer_value_label = tk.Label(
            dealer_frame,
            text="Value: 0",
            font=('Arial', 11),
            bg='#1A5A1A',
            fg='#BDC3C7'
        )
        self.dealer_value_label.pack(pady=2)
        
        # Players section
        players_frame = tk.Frame(main_frame, bg=self.CARD_COLORS['background'])
        players_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.player_frames: List[tk.Frame] = []
        self.player_hand_labels: List[tk.Label] = []
        self.player_value_labels: List[tk.Label] = []
        self.player_chips_labels: List[tk.Label] = []
        self.player_bet_labels: List[tk.Label] = []
        
        for i, player in enumerate(self.game.players):
            player_frame = tk.Frame(players_frame, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
            player_frame.pack(pady=5, padx=10, fill=tk.X)
            self.player_frames.append(player_frame)
            
            # Player name and chips
            name_frame = tk.Frame(player_frame, bg='#1A5A1A')
            name_frame.pack(pady=5, padx=10, fill=tk.X)
            
            name_label = tk.Label(
                name_frame,
                text=f"{player.name}",
                font=('Arial', 14, 'bold'),
                bg='#1A5A1A',
                fg='white'
            )
            name_label.pack(side=tk.LEFT, padx=5)
            
            chips_label = tk.Label(
                name_frame,
                text=f"Chips: {player.chips}",
                font=('Arial', 11),
                bg='#1A5A1A',
                fg='#F39C12'
            )
            chips_label.pack(side=tk.LEFT, padx=10)
            self.player_chips_labels.append(chips_label)
            
            bet_label = tk.Label(
                name_frame,
                text="Bet: 0",
                font=('Arial', 11),
                bg='#1A5A1A',
                fg='#3498DB'
            )
            bet_label.pack(side=tk.LEFT, padx=10)
            self.player_bet_labels.append(bet_label)
            
            # Hand display
            hand_label = tk.Label(
                player_frame,
                text="No cards",
                font=('Arial', 11),
                bg='#1A5A1A',
                fg='white'
            )
            hand_label.pack(pady=5)
            self.player_hand_labels.append(hand_label)
            
            value_label = tk.Label(
                player_frame,
                text="Value: 0",
                font=('Arial', 10),
                bg='#1A5A1A',
                fg='#BDC3C7'
            )
            value_label.pack(pady=2)
            self.player_value_labels.append(value_label)
        
        # Action buttons frame
        action_frame = tk.Frame(self.root, bg=self.CARD_COLORS['background'])
        action_frame.pack(pady=10)
        
        self.hit_button = tk.Button(
            action_frame,
            text="Hit",
            command=self.hit,
            font=('Arial', 14, 'bold'),
            bg='#E74C3C',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2',
            state=tk.DISABLED
        )
        self.hit_button.pack(side=tk.LEFT, padx=10)
        
        self.stand_button = tk.Button(
            action_frame,
            text="Stand",
            command=self.stand,
            font=('Arial', 14, 'bold'),
            bg='#3498DB',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2',
            state=tk.DISABLED
        )
        self.stand_button.pack(side=tk.LEFT, padx=10)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg=self.CARD_COLORS['background'])
        control_frame.pack(pady=10)
        
        self.new_round_button = tk.Button(
            control_frame,
            text="New Round",
            command=self.start_new_round,
            font=('Arial', 12, 'bold'),
            bg='#27AE60',
            fg='white',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.new_round_button.pack(side=tk.LEFT, padx=10)
        
        self.new_deck_button = tk.Button(
            control_frame,
            text="New Deck",
            command=self.use_new_deck,
            font=('Arial', 12, 'bold'),
            bg='#9B59B6',
            fg='white',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.new_deck_button.pack(side=tk.LEFT, padx=10)
        
        self.quit_button = tk.Button(
            control_frame,
            text="Quit Game",
            command=self.quit_game,
            font=('Arial', 12, 'bold'),
            bg='#95A5A6',
            fg='white',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)
        
        # Results text area
        results_frame = tk.Frame(self.root, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
        results_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.results_text = tk.Text(
            results_frame,
            height=6,
            font=('Arial', 10),
            bg='#2C3E50',
            fg='white',
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.results_text.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        
        # Start first round
        self.update_display()
        self.update_status("Click 'New Round' to start playing!")
    
    def format_cards(self, cards: List[PlayingCard]) -> str:
        """Format cards for display."""
        if not cards:
            return "No cards"
        return "  ".join(str(card) for card in cards)
    
    def update_display(self):
        """Update the display with current game state."""
        if not self.game:
            return
        
        # Update round label
        self.round_label.config(text=f"Round {self.game.round_number}")
        
        # Update dealer display
        dealer_cards = self.format_cards(self.game.dealer.hand.cards)
        dealer_value = self.game.dealer.hand.calculate_value()
        
        # Hide dealer's hole card if round in progress
        if self.round_in_progress and len(self.game.dealer.hand.cards) > 1:
            visible_cards = [str(self.game.dealer.hand.cards[0])]
            for card in self.game.dealer.hand.cards[1:]:
                visible_cards.append("XX" if not card.faceup else str(card))
            dealer_cards = "  ".join(visible_cards)
            if not self.game.dealer.hand.cards[1].faceup:
                dealer_value = self.game.dealer.hand.cards[0].rank.value
                if dealer_value >= 11:
                    dealer_value = 10
                elif dealer_value == 1:
                    dealer_value = 11
        
        self.dealer_hand_label.config(text=dealer_cards)
        
        dealer_status = ""
        if self.game.dealer.blackjack:
            dealer_status = " (BLACKJACK!)"
        elif self.game.dealer.busted:
            dealer_status = " (BUST)"
        
        self.dealer_value_label.config(text=f"Value: {dealer_value}{dealer_status}")
        
        # Update players display
        for i, player in enumerate(self.game.players):
            # Update chips and bet
            self.player_chips_labels[i].config(text=f"Chips: {player.chips}")
            self.player_bet_labels[i].config(text=f"Bet: {player.bet}")
            
            # Update hand
            cards_str = self.format_cards(player.hand.cards)
            self.player_hand_labels[i].config(text=cards_str if cards_str else "No cards")
            
            # Update value
            value = player.hand.calculate_value()
            status = ""
            if player.blackjack:
                status = " (BLACKJACK!)"
            elif player.busted:
                status = " (BUST)"
            elif player.stand:
                status = " (STAND)"
            
            self.player_value_labels[i].config(text=f"Value: {value}{status}")
            
            # Highlight current player
            if i == self.current_player_index and self.waiting_for_action:
                self.player_frames[i].config(bg='#2E7D32')
            else:
                self.player_frames[i].config(bg='#1A5A1A')
    
    def update_status(self, message: str):
        """Update the status label."""
        self.status_label.config(text=message)
    
    def log_message(self, message: str):
        """Add a message to the results text area."""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.insert(tk.END, message + "\n")
        self.results_text.see(tk.END)
        self.results_text.config(state=tk.DISABLED)
    
    def collect_bets(self) -> bool:
        """Collect bets from all players."""
        active_players = [p for p in self.game.players if p.chips >= self.game.MIN_BET]
        
        if not active_players:
            messagebox.showinfo("No Players", "No players have enough chips to play!")
            return False
        
        for player in self.game.players:
            if player.chips < self.game.MIN_BET:
                continue
            
            while True:
                bet_str = simpledialog.askstring(
                    "Place Bet",
                    f"{player.name}, enter your bet:\n(Min: {self.game.MIN_BET}, Max: {player.chips})",
                    initialvalue=str(self.game.MIN_BET)
                )
                
                if bet_str is None:  # User cancelled
                    return False
                
                try:
                    bet = int(bet_str)
                    if bet < self.game.MIN_BET:
                        messagebox.showerror("Invalid Bet", f"Minimum bet is {self.game.MIN_BET}")
                        continue
                    if bet > player.chips:
                        messagebox.showerror("Invalid Bet", f"You only have {player.chips} chips")
                        continue
                    
                    player.place_bet(bet)
                    self.log_message(f"{player.name} bets {bet} chips")
                    break
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter a valid number")
        
        return True
    
    def start_new_round(self):
        """Start a new round."""
        if self.round_in_progress:
            messagebox.showinfo("Round in Progress", "Please finish the current round first!")
            return
        
        # Check if players can play
        active_players = [p for p in self.game.players if p.chips >= self.game.MIN_BET]
        if not active_players:
            messagebox.showinfo("Game Over", "No players have enough chips to continue playing!")
            return
        
        self.game.round_number += 1
        self.log_message(f"\n{'='*60}")
        self.log_message(f"Round {self.game.round_number}")
        self.log_message(f"{'='*60}")
        
        # Reset hands
        for player in self.game.players:
            player.reset_hand()
        self.game.dealer.reset_hand()
        
        # Collect bets
        if not self.collect_bets():
            self.game.round_number -= 1
            return
        
        # Check if any bets were placed
        if not any(p.bet > 0 for p in self.game.players):
            self.log_message("No bets placed. Round cancelled.")
            self.game.round_number -= 1
            return
        
        # Deal initial cards
        self.game._deal_initial_cards()
        self.round_in_progress = True
        
        # Check for dealer blackjack
        if self.game.dealer.blackjack:
            self.log_message("Dealer has BLACKJACK!")
            self.resolve_round()
            return
        
        # Start player turns
        self.current_player_index = 0
        self.start_next_player_turn()
        self.update_display()
    
    def start_next_player_turn(self):
        """Start the next player's turn."""
        # Find next active player
        while self.current_player_index < len(self.game.players):
            player = self.game.players[self.current_player_index]
            if player.bet > 0 and player.can_play() and not player.blackjack:
                self.waiting_for_action = True
                self.update_status(f"{player.name}'s turn - Choose Hit or Stand")
                self.hit_button.config(state=tk.NORMAL)
                self.stand_button.config(state=tk.NORMAL)
                self.update_display()
                return
            self.current_player_index += 1
        
        # All players done, dealer's turn
        self.waiting_for_action = False
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.dealer_turn()
    
    def hit(self):
        """Player chooses to hit."""
        if not self.waiting_for_action:
            return
        
        player = self.game.players[self.current_player_index]
        if not player.can_play():
            return
        
        # Deal a card
        card = self.game.deck.deal()
        card.faceup = True
        player.hand.add_card(card)
        
        self.log_message(f"{player.name} draws: {card}")
        self.update_display()
        
        if player.hand.is_bust():
            player.busted = True
            self.log_message(f"{player.name} BUSTS!")
            self.current_player_index += 1
            self.start_next_player_turn()
        elif player.hand.is_blackjack() and len(player.hand.cards) == 2:
            player.blackjack = True
            player.stand = True
            self.log_message(f"{player.name} has BLACKJACK!")
            self.current_player_index += 1
            self.start_next_player_turn()
        else:
            # Still player's turn, wait for next action
            pass
    
    def stand(self):
        """Player chooses to stand."""
        if not self.waiting_for_action:
            return
        
        player = self.game.players[self.current_player_index]
        if not player.can_play():
            return
        
        player.stand = True
        self.log_message(f"{player.name} stands")
        self.current_player_index += 1
        self.start_next_player_turn()
    
    def dealer_turn(self):
        """Handle dealer's turn."""
        # Check if any players are still in
        if not any(p.bet > 0 and not p.busted for p in self.game.players):
            self.resolve_round()
            return
        
        # Show dealer's hole card
        if len(self.game.dealer.hand.cards) > 1:
            self.game.dealer.hand.cards[1].faceup = True
        
        self.log_message("\nDealer's turn")
        self.update_display()
        
        # Check for dealer blackjack
        if self.game.dealer.hand.is_blackjack():
            self.game.dealer.blackjack = True
            self.log_message("Dealer has BLACKJACK!")
            self.resolve_round()
            return
        
        # Dealer hits until 17 or more
        while self.game.dealer.should_hit():
            card = self.game.deck.deal()
            card.faceup = True
            self.game.dealer.hand.add_card(card)
            self.log_message(f"Dealer draws: {card}")
            self.update_display()
            self.root.update()
            self.root.after(1000)  # Small delay for visual effect
            
            if self.game.dealer.hand.is_bust():
                self.game.dealer.busted = True
                self.log_message("Dealer BUSTS!")
                break
        
        if not self.game.dealer.busted:
            self.log_message("Dealer stands")
        
        self.resolve_round()
    
    def resolve_round(self):
        """Resolve the round and distribute winnings."""
        self.log_message(f"\n{'='*60}")
        self.log_message("ROUND RESULTS")
        self.log_message(f"{'='*60}")
        
        dealer_value = self.game.dealer.hand.calculate_value()
        self.log_message(f"\nDealer's final value: {dealer_value}")
        if self.game.dealer.busted:
            self.log_message("Dealer BUSTED - All remaining players win!")
        elif self.game.dealer.blackjack:
            self.log_message("Dealer has BLACKJACK!")
        
        self.log_message("\nPlayer Results:")
        for player in self.game.players:
            if player.bet == 0:
                continue
            
            winnings = self.game._calculate_winnings(player)
            player.win(winnings)
            net = winnings - player.bet
            
            result = ""
            if player.busted:
                result = "BUST - Lost"
            elif player.blackjack and not self.game.dealer.blackjack:
                result = "BLACKJACK - Won"
            elif self.game.dealer.busted:
                result = "Won (Dealer busted)"
            elif player.hand.calculate_value() > dealer_value:
                result = "Won"
            elif player.hand.calculate_value() < dealer_value:
                result = "Lost"
            else:
                result = "Push (Tie)"
            
            self.log_message(f"{player.name}: {result}")
            self.log_message(f"  Bet: {player.bet}, Winnings: {winnings}, Net: {net:+d}")
            self.log_message(f"  New chip count: {player.chips}")
        
        self.round_in_progress = False
        self.waiting_for_action = False
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.update_display()
        self.update_status("Round complete! Click 'New Round' to play again.")
        
        # Check deck size
        if not self.game._check_deck_size():
            self.log_message(f"\nWarning: Only {len(self.game.deck)} cards remaining in deck.")
    
    def use_new_deck(self):
        """Create and shuffle a new deck."""
        if self.round_in_progress:
            messagebox.showinfo("Round in Progress", "Please finish the current round first!")
            return
        
        self.game.use_new_deck()
        self.log_message("New deck created and shuffled!")
        messagebox.showinfo("New Deck", "New deck created and shuffled!")
    
    def quit_game(self):
        """Quit the game."""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            self.root.quit()


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

