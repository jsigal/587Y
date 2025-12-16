"""
Poker game - GUI Version
Graphical user interface implementation using tkinter.
"""
from __future__ import annotations
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import List, Optional
from poker import PokerGame, Player, PokerHand, HumanPlayerStrategy, AIPlayerStrategy
from cardlib_enum import PlayingCard


class PokerGUI:
    """Graphical user interface for Poker game."""
    
    CARD_COLORS = {
        'red': '#DC143C',      # Crimson for hearts/diamonds
        'black': '#000000',    # Black for clubs/spades
        'background': '#0D4F0D',  # Dark green table
        'card_bg': '#FFFFFF',  # White card background
        'text': '#000000',
        'highlight': '#FFD700',  # Gold for highlights
        'selected': '#90EE90'   # Light green for selected cards
    }
    
    def __init__(self, root):
        self.root = root
        self.root.title("5-Card Draw Poker")
        self.root.geometry("1200x900")
        self.root.configure(bg=self.CARD_COLORS['background'])
        
        # Game state
        self.game: Optional[PokerGame] = None
        self.current_phase = "setup"  # setup, betting, discard, showdown
        self.selected_cards: List[int] = []  # For discard selection
        self.betting_action_pending = False
        self.waiting_for_discard = False
        
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
            text="5-CARD DRAW POKER",
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
        
        self.num_players_var = tk.IntVar(value=2)
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
            "• 5-Card Draw Poker with betting rounds\n"
            "• Small Blind: 10 chips, Big Blind: 20 chips\n"
            "• Each player receives 5 cards\n"
            "• Pre-draw betting round\n"
            "• Discard 0-3 cards and draw replacements\n"
            "• Post-draw betting round\n"
            "• Showdown: Best hand wins\n"
            "• Hand rankings: High Card < Pair < Two Pair < Three of a Kind <\n"
            "  Straight < Flush < Full House < Four of a Kind <\n"
            "  Straight Flush < Royal Flush"
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
            
            if starting_chips < 20:
                messagebox.showerror("Error", "Starting chips must be at least 20!")
                return
            
            self.game = PokerGame(num_players, starting_chips)
            self.current_phase = "setup"
            self.selected_cards = []
            
            # Create game screen
            self.create_game_screen()
            self.play_hand()
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
            text="5-CARD DRAW POKER",
            font=('Arial', 24, 'bold'),
            bg=self.CARD_COLORS['background'],
            fg='white'
        )
        title_label.pack(pady=10)
        
        # Game info frame
        info_frame = tk.Frame(self.root, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
        info_frame.pack(pady=5, padx=20, fill=tk.X)
        
        self.phase_label = tk.Label(
            info_frame,
            text="Ready to play!",
            font=('Arial', 14, 'bold'),
            bg='#1A5A1A',
            fg='#F39C12'
        )
        self.phase_label.pack(pady=5)
        
        self.status_label = tk.Label(
            info_frame,
            text="",
            font=('Arial', 12),
            bg='#1A5A1A',
            fg='white'
        )
        self.status_label.pack(pady=5)
        
        # Pot and betting info
        pot_frame = tk.Frame(info_frame, bg='#1A5A1A')
        pot_frame.pack(pady=5)
        
        self.pot_label = tk.Label(
            pot_frame,
            text="Pot: 0 chips",
            font=('Arial', 12, 'bold'),
            bg='#1A5A1A',
            fg='#FFD700'
        )
        self.pot_label.pack(side=tk.LEFT, padx=10)
        
        self.current_bet_label = tk.Label(
            pot_frame,
            text="Current Bet: 0 chips",
            font=('Arial', 12),
            bg='#1A5A1A',
            fg='white'
        )
        self.current_bet_label.pack(side=tk.LEFT, padx=10)
        
        # Main content frame (scrollable)
        main_frame = tk.Frame(self.root, bg=self.CARD_COLORS['background'])
        main_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Players section
        players_frame = tk.Frame(main_frame, bg=self.CARD_COLORS['background'])
        players_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.player_frames: List[tk.Frame] = []
        self.player_card_frames: List[tk.Frame] = []
        self.player_card_labels: List[List[tk.Label]] = []
        self.player_info_labels: List[tk.Label] = []
        self.player_chips_labels: List[tk.Label] = []
        self.player_bet_labels: List[tk.Label] = []
        self.player_hand_labels: List[tk.Label] = []
        
        for i, player in enumerate(self.game.players):
            player_frame = tk.Frame(players_frame, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
            player_frame.pack(pady=5, padx=10, fill=tk.X)
            self.player_frames.append(player_frame)
            
            # Player name and status
            name_frame = tk.Frame(player_frame, bg='#1A5A1A')
            name_frame.pack(pady=5, padx=10, fill=tk.X)
            
            name_label = tk.Label(
                name_frame,
                text=f"{player.name}" + (" (You)" if i == 0 else ""),
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
            
            status_label = tk.Label(
                name_frame,
                text="",
                font=('Arial', 11),
                bg='#1A5A1A',
                fg='#E74C3C'
            )
            status_label.pack(side=tk.LEFT, padx=10)
            
            # Card display frame
            card_frame = tk.Frame(player_frame, bg='#1A5A1A')
            card_frame.pack(pady=5, padx=10)
            self.player_card_frames.append(card_frame)
            
            card_labels = []
            for j in range(5):
                card_label = tk.Label(
                    card_frame,
                    text="XX",
                    font=('Courier', 16, 'bold'),
                    bg=self.CARD_COLORS['card_bg'],
                    fg=self.CARD_COLORS['black'],
                    width=4,
                    height=2,
                    relief=tk.RAISED,
                    borderwidth=2
                )
                card_label.pack(side=tk.LEFT, padx=3)
                card_labels.append(card_label)
            self.player_card_labels.append(card_labels)
            
            # Hand rank display
            hand_label = tk.Label(
                player_frame,
                text="",
                font=('Arial', 11),
                bg='#1A5A1A',
                fg='#2ECC71'
            )
            hand_label.pack(pady=2)
            self.player_hand_labels.append(hand_label)
            
            info_label = tk.Label(
                player_frame,
                text="",
                font=('Arial', 10),
                bg='#1A5A1A',
                fg='#BDC3C7'
            )
            info_label.pack(pady=2)
            self.player_info_labels.append(info_label)
        
        # Action frame (for human player actions)
        self.action_frame = tk.Frame(self.root, bg=self.CARD_COLORS['background'])
        self.action_frame.pack(pady=10, padx=20, fill=tk.X)
        
        # Betting buttons
        self.betting_frame = tk.Frame(self.action_frame, bg=self.CARD_COLORS['background'])
        
        self.fold_button = tk.Button(
            self.betting_frame,
            text="Fold",
            command=self.action_fold,
            font=('Arial', 12),
            bg='#E74C3C',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.fold_button.pack(side=tk.LEFT, padx=5)
        
        self.check_call_button = tk.Button(
            self.betting_frame,
            text="Check/Call",
            command=self.action_check_call,
            font=('Arial', 12),
            bg='#3498DB',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.check_call_button.pack(side=tk.LEFT, padx=5)
        
        self.raise_frame = tk.Frame(self.betting_frame, bg=self.CARD_COLORS['background'])
        self.raise_frame.pack(side=tk.LEFT, padx=5)
        
        raise_label = tk.Label(
            self.raise_frame,
            text="Raise:",
            font=('Arial', 11),
            bg=self.CARD_COLORS['background'],
            fg='white'
        )
        raise_label.pack(side=tk.LEFT, padx=5)
        
        self.raise_var = tk.IntVar(value=50)
        raise_entry = tk.Entry(
            self.raise_frame,
            textvariable=self.raise_var,
            font=('Arial', 11),
            width=8
        )
        raise_entry.pack(side=tk.LEFT, padx=5)
        
        self.raise_button = tk.Button(
            self.betting_frame,
            text="Raise",
            command=self.action_raise,
            font=('Arial', 12),
            bg='#27AE60',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.raise_button.pack(side=tk.LEFT, padx=5)
        
        # Discard frame (for discard phase)
        self.discard_frame = tk.Frame(self.action_frame, bg=self.CARD_COLORS['background'])
        
        self.discard_button = tk.Button(
            self.discard_frame,
            text="Discard Selected",
            command=self.action_discard,
            font=('Arial', 12),
            bg='#9B59B6',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.discard_button.pack(side=tk.LEFT, padx=5)
        
        self.keep_all_button = tk.Button(
            self.discard_frame,
            text="Keep All Cards",
            command=self.action_keep_all,
            font=('Arial', 12),
            bg='#16A085',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.keep_all_button.pack(side=tk.LEFT, padx=5)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg=self.CARD_COLORS['background'])
        control_frame.pack(pady=10)
        
        self.next_hand_button = tk.Button(
            control_frame,
            text="Next Hand",
            command=self.next_hand,
            font=('Arial', 12),
            bg='#95A5A6',
            fg='white',
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.next_hand_button.pack(side=tk.LEFT, padx=5)
        
        self.new_game_button = tk.Button(
            control_frame,
            text="New Game",
            command=self.new_game,
            font=('Arial', 12),
            bg='#34495E',
            fg='white',
            padx=20,
            pady=10
        )
        self.new_game_button.pack(side=tk.LEFT, padx=5)
        
        # Log/Message area
        log_frame = tk.Frame(self.root, bg='#1A5A1A', relief=tk.RIDGE, borderwidth=2)
        log_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        log_label = tk.Label(
            log_frame,
            text="Game Log:",
            font=('Arial', 12, 'bold'),
            bg='#1A5A1A',
            fg='white'
        )
        log_label.pack(pady=5)
        
        self.log_text = tk.Text(
            log_frame,
            height=8,
            font=('Courier', 10),
            bg='#2C3E50',
            fg='#ECF0F1',
            wrap=tk.WORD
        )
        self.log_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)
    
    def log_message(self, message: str):
        """Add a message to the log."""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def format_cards(self, cards: List[PlayingCard]) -> str:
        """Format cards for display."""
        if not cards:
            return "No cards"
        return "  ".join(str(card) for card in cards)
    
    def update_display(self):
        """Update all player displays."""
        if not self.game:
            return
        
        # Safety check: ensure GUI lists are initialized and match player count
        if (not hasattr(self, 'player_chips_labels') or 
            len(self.player_chips_labels) != len(self.game.players)):
            return
        
        # Update pot and current bet
        self.pot_label.config(text=f"Pot: {self.game.pot} chips")
        self.current_bet_label.config(text=f"Current Bet: {self.game.current_bet} chips")
        
        # Update each player's display
        for i, player in enumerate(self.game.players):
            # Update chips and bet
            self.player_chips_labels[i].config(text=f"Chips: {player.chips}")
            bet_text = f"Bet: {player.current_bet}"
            if player.total_bet_this_round > 0:
                bet_text += f" (total: {player.total_bet_this_round})"
            self.player_bet_labels[i].config(text=bet_text)
            
            # Update cards
            is_human = i == 0
            is_current_player = (self.current_phase == "betting" and 
                                hasattr(self, 'current_betting_player') and
                                self.current_betting_player == player)
            
            # Show cards face up for human player or when showing all
            show_cards = is_human or self.current_phase == "showdown"
            
            for j in range(5):
                card_label = self.player_card_labels[i][j]
                if j < len(player.cards):
                    card = player.cards[j]
                    if show_cards:
                        card_text = str(card)
                        # Color code by suit
                        if card.suit.symbol in ['♥', '♦']:
                            card_label.config(fg=self.CARD_COLORS['red'])
                        else:
                            card_label.config(fg=self.CARD_COLORS['black'])
                    else:
                        card_text = "XX"
                        card_label.config(fg=self.CARD_COLORS['black'])
                    
                    card_label.config(text=card_text)
                    
                    # Highlight selected cards for discard
                    if is_human and j in self.selected_cards and self.current_phase == "discard":
                        card_label.config(bg=self.CARD_COLORS['selected'])
                    elif is_human and self.current_phase == "discard":
                        card_label.config(bg=self.CARD_COLORS['card_bg'])
                    else:
                        card_label.config(bg=self.CARD_COLORS['card_bg'])
                    
                    # Make cards clickable for discard selection (human player only)
                    if is_human and self.current_phase == "discard" and self.waiting_for_discard:
                        card_label.config(cursor='hand2')
                        card_label.bind('<Button-1>', lambda e, idx=j: self.toggle_card_selection(idx))
                    else:
                        card_label.config(cursor='')
                        card_label.unbind('<Button-1>')
                else:
                    card_label.config(text="", bg=self.CARD_COLORS['card_bg'])
            
            # Update hand rank
            if player.hand and (show_cards or is_human):
                self.player_hand_labels[i].config(text=f"Hand: {player.hand.hand_name}")
            else:
                self.player_hand_labels[i].config(text="")
            
            # Update status info
            status_parts = []
            if player.folded:
                status_parts.append("FOLDED")
            if player.all_in:
                status_parts.append("ALL-IN")
            if is_current_player:
                status_parts.append("← YOUR TURN")
            
            self.player_info_labels[i].config(
                text=" | ".join(status_parts) if status_parts else ""
            )
            
            # Highlight current player frame
            if is_current_player:
                self.player_frames[i].config(relief=tk.RAISED, borderwidth=4)
            else:
                self.player_frames[i].config(relief=tk.RIDGE, borderwidth=2)
    
    def toggle_card_selection(self, card_index: int):
        """Toggle card selection for discarding."""
        if self.current_phase != "discard" or not self.waiting_for_discard:
            return
        
        if card_index in self.selected_cards:
            self.selected_cards.remove(card_index)
        else:
            if len(self.selected_cards) < 3:
                self.selected_cards.append(card_index)
            else:
                messagebox.showinfo("Info", "You can discard at most 3 cards!")
                return
        
        self.update_display()
        self.log_message(f"Selected {len(self.selected_cards)} card(s) to discard")
    
    def play_hand(self):
        """Play a complete hand."""
        if not self.game:
            return
        
        self.current_phase = "new_hand"
        self.game._reset_for_new_hand()
        self.game.deal_hands()
        
        self.log_message("\n" + "="*70)
        self.log_message("NEW HAND")
        self.log_message("="*70)
        self.update_display()
        
        # Pre-draw betting round
        self.current_phase = "betting"
        self.phase_label.config(text="PRE-DRAW BETTING ROUND")
        self.run_betting_round("PRE-DRAW")
        
        active_players = [p for p in self.game.players if p.is_active]
        if len(active_players) <= 1:
            self.handle_early_winner()
            return
        
        # Discard phase
        self.current_phase = "discard"
        self.phase_label.config(text="DISCARD AND DRAW PHASE")
        self.run_discard_phase()
        
        active_players = [p for p in self.game.players if p.is_active]
        if len(active_players) <= 1:
            self.handle_early_winner()
            return
        
        # Post-draw betting round
        self.current_phase = "betting"
        self.phase_label.config(text="POST-DRAW BETTING ROUND")
        self.run_betting_round("POST-DRAW")
        
        active_players = [p for p in self.game.players if p.is_active]
        if len(active_players) <= 1:
            self.handle_early_winner()
            return
        
        # Showdown
        self.current_phase = "showdown"
        self.phase_label.config(text="SHOWDOWN")
        self.showdown()
        
        # Show final chip counts
        self.log_message("\n" + "="*70)
        self.log_message("FINAL CHIP COUNTS:")
        for player in self.game.players:
            self.log_message(f"{player.name}: {player.chips} chips")
        self.log_message("="*70)
        
        self.update_display()
        self.next_hand_button.config(state=tk.NORMAL)
    
    def run_betting_round(self, round_name: str):
        """Run a betting round with GUI interaction."""
        self.log_message(f"\n{round_name} BETTING ROUND")
        
        # Reset betting states
        for player in self.game.players:
            player.reset_betting_state()
        self.game.current_bet = 0
        
        # Post blinds if pre-draw
        current_player_index = 0
        if round_name == "PRE-DRAW":
            active_players = [p for p in self.game.players if p.is_active]
            if len(active_players) >= 2:
                sb_player = active_players[0]
                bb_player = active_players[1]
                
                sb_bet = min(self.game.small_blind, sb_player.chips)
                bb_bet = min(self.game.big_blind, bb_player.chips)
                
                if sb_bet > 0:
                    actual = sb_player.bet(sb_bet)
                    self.game.pot += actual
                    self.log_message(f"{sb_player.name} posts small blind: {sb_bet}")
                
                if bb_bet > 0:
                    actual = bb_player.bet(bb_bet)
                    self.game.pot += bb_bet
                    self.log_message(f"{bb_player.name} posts big blind: {bb_bet}")
                
                self.game.current_bet = max(sb_player.current_bet, bb_player.current_bet)
                
                # Find the index of the big blind player and start from the next player
                bb_index = self.game.players.index(bb_player)
                current_player_index = (bb_index + 1) % len(self.game.players)
        
        self.update_display()
        
        # Betting loop
        iteration = 0
        max_iterations = len(self.game.players) * 10
        
        while iteration < max_iterations:
            active_players = [p for p in self.game.players if p.can_bet]
            
            if len(active_players) <= 1:
                break
            
            # Check if betting is complete
            all_matched = all(
                p.current_bet == self.game.current_bet or p.all_in
                for p in self.game.players if p.is_active
            )
            if all_matched and iteration > 1:
                break
            
            player = self.game.players[current_player_index]
            
            if not player.can_bet:
                current_player_index = (current_player_index + 1) % len(self.game.players)
                iteration += 1
                continue
            
            self.current_betting_player = player
            self.update_display()
            
            if isinstance(player.strategy, HumanPlayerStrategy):
                # Human player turn
                self.wait_for_human_betting_action(player)
            else:
                # AI player turn - process immediately
                action = player.strategy.get_betting_action(player, self.game.current_bet)
                self.process_betting_action(action, player, current_player_index)
                self.root.update()  # Update display to show AI action
            
            current_player_index = (current_player_index + 1) % len(self.game.players)
            iteration += 1
        
        self.update_display()
    
    def wait_for_human_betting_action(self, player: Player):
        """Enable betting buttons and wait for human action."""
        self.betting_action_pending = True
        
        call_amount = self.game.current_bet - player.current_bet
        max_raise = min(player.chips - call_amount, player.chips) if call_amount < player.chips else 0
        
        if call_amount == 0:
            self.check_call_button.config(text="Check", state=tk.NORMAL)
        else:
            self.check_call_button.config(text=f"Call ({call_amount})", state=tk.NORMAL)
        
        self.fold_button.config(state=tk.NORMAL)
        self.raise_button.config(state=tk.NORMAL)
        self.betting_frame.pack(pady=10)
        self.discard_frame.pack_forget()
        
        self.status_label.config(
            text=f"{player.name}'s turn - {player.chips} chips - Current bet to match: {self.game.current_bet}"
        )
        
        if player.hand:
            self.log_message(f"\nYour hand: {self.format_cards(player.cards)} - {player.hand.hand_name}")
        
        # Wait for action
        while self.betting_action_pending:
            self.root.update()
    
    def process_ai_betting_action(self, player: Player):
        """Process AI player's betting action."""
        action = player.strategy.get_betting_action(player, self.game.current_bet)
        
        # Find player index
        player_index = self.game.players.index(player)
        
        self.process_betting_action(action, player, player_index)
    
    def process_betting_action(self, action: str, player: Player, player_index: int):
        """Process a betting action."""
        if action == "fold":
            player.fold()
            self.log_message(f"{player.name} folds")
        elif action == "call":
            call_amount = self.game.current_bet - player.current_bet
            if call_amount > 0:
                actual_bet = player.bet(call_amount)
                self.game.pot += actual_bet
                self.log_message(f"{player.name} calls {actual_bet} chips")
            else:
                self.log_message(f"{player.name} checks")
        elif action.startswith("raise"):
            raise_amount = int(action.split()[1])
            total_needed = self.game.current_bet - player.current_bet + raise_amount
            actual_bet = player.bet(total_needed)
            self.game.pot += actual_bet
            self.game.current_bet = player.current_bet
            self.log_message(f"{player.name} raises by {raise_amount} chips (total bet: {player.current_bet})")
        
        self.update_display()
    
    def action_fold(self):
        """Handle fold action."""
        if not self.betting_action_pending:
            return
        
        self.betting_action_pending = False
        player = self.current_betting_player
        player_index = self.game.players.index(player)
        
        self.betting_frame.pack_forget()
        self.process_betting_action("fold", player, player_index)
    
    def action_check_call(self):
        """Handle check/call action."""
        if not self.betting_action_pending:
            return
        
        self.betting_action_pending = False
        player = self.current_betting_player
        player_index = self.game.players.index(player)
        
        self.betting_frame.pack_forget()
        self.process_betting_action("call", player, player_index)
    
    def action_raise(self):
        """Handle raise action."""
        if not self.betting_action_pending:
            return
        
        player = self.current_betting_player
        player_index = self.game.players.index(player)
        raise_amount = self.raise_var.get()
        call_amount = self.game.current_bet - player.current_bet
        max_raise = min(player.chips - call_amount, player.chips) if call_amount < player.chips else player.chips
        
        if raise_amount < 0:
            messagebox.showerror("Error", "Raise amount must be positive")
            return
        
        if call_amount + raise_amount > player.chips:
            messagebox.showerror("Error", f"Not enough chips. Maximum raise: {max_raise}")
            return
        
        self.betting_action_pending = False
        self.betting_frame.pack_forget()
        self.process_betting_action(f"raise {raise_amount}", player, player_index)
    
    def run_discard_phase(self):
        """Run the discard and draw phase."""
        self.log_message("\nDISCARD AND DRAW PHASE")
        
        all_discards = []
        
        for player in self.game.players:
            if not player.is_active:
                continue
            
            self.update_display()
            
            if isinstance(player.strategy, HumanPlayerStrategy):
                # Human player discard
                self.wait_for_human_discard(player)
                discard_indices = self.selected_cards.copy()
                self.selected_cards = []
            else:
                # AI player discard
                discard_indices = player.strategy.get_discard_decision(player)
            
            # Discard cards
            discard_count = 0
            for idx in sorted(discard_indices, reverse=True):
                if 0 <= idx < len(player.cards):
                    discarded = player.cards.pop(idx)
                    all_discards.append(discarded)
                    discard_count += 1
            
            if discard_count > 0:
                self.log_message(f"{player.name} discards {discard_count} card(s)")
            else:
                self.log_message(f"{player.name} keeps all cards")
        
        # Return discards to deck and shuffle
        for card in all_discards:
            self.game.deck.add(card)
        self.game.deck.shuffle()
        
        # Draw replacement cards
        for player in self.game.players:
            if not player.is_active:
                continue
            
            cards_to_draw = 5 - len(player.cards)
            
            for _ in range(cards_to_draw):
                new_card = self.game.deck.deal()
                new_card.faceup = True
                player.cards.append(new_card)
            
            # Re-evaluate hand
            if len(player.cards) == 5:
                player.hand = PokerHand(player.name, player.cards)
            
            if isinstance(player.strategy, HumanPlayerStrategy) and cards_to_draw > 0:
                self.log_message(f"Drew {cards_to_draw} new card(s)")
                self.log_message(f"Your new hand: {self.format_cards(player.cards)}")
        
        self.update_display()
    
    def wait_for_human_discard(self, player: Player):
        """Enable discard interface and wait for human action."""
        self.waiting_for_discard = True
        self.selected_cards = []
        
        self.betting_frame.pack_forget()
        self.discard_frame.pack(pady=10)
        self.discard_button.config(state=tk.NORMAL)
        self.keep_all_button.config(state=tk.NORMAL)
        
        self.status_label.config(
            text=f"{player.name}'s turn - Select up to 3 cards to discard, or keep all"
        )
        self.log_message(f"\nYour hand: {self.format_cards(player.cards)}")
        if player.hand:
            self.log_message(f"Hand rank: {player.hand.hand_name}")
        
        self.update_display()
        
        # Wait for discard action
        discard_action_pending = True
        
        def on_discard():
            nonlocal discard_action_pending
            if len(self.selected_cards) > 3:
                messagebox.showinfo("Info", "You can discard at most 3 cards!")
                return
            discard_action_pending = False
            self.waiting_for_discard = False
            self.discard_button.config(state=tk.DISABLED)
            self.keep_all_button.config(state=tk.DISABLED)
            self.discard_frame.pack_forget()
        
        def on_keep_all():
            nonlocal discard_action_pending
            self.selected_cards = []
            discard_action_pending = False
            self.waiting_for_discard = False
            self.discard_button.config(state=tk.DISABLED)
            self.keep_all_button.config(state=tk.DISABLED)
            self.discard_frame.pack_forget()
        
        self.discard_button.config(command=on_discard)
        self.keep_all_button.config(command=on_keep_all)
        
        while discard_action_pending:
            self.root.update()
        
        self.discard_button.config(command=self.action_discard)
        self.keep_all_button.config(command=self.action_keep_all)
    
    def action_discard(self):
        """Handle discard action."""
        if len(self.selected_cards) > 3:
            messagebox.showinfo("Info", "You can discard at most 3 cards!")
            return
        self.waiting_for_discard = False
    
    def action_keep_all(self):
        """Handle keep all cards action."""
        self.selected_cards = []
        self.waiting_for_discard = False
    
    def showdown(self):
        """Execute showdown and determine winner."""
        self.log_message("\n" + "="*70)
        self.log_message("SHOWDOWN - RESULTS:")
        self.log_message("="*70)
        
        # Show all hands
        self.log_message("\nAll players' hands:")
        for player in self.game.players:
            if not player.is_active:
                self.log_message(f"{player.name}: FOLDED")
            elif player.hand:
                cards_str = self.format_cards(player.cards)
                self.log_message(f"{player.name}: {cards_str} - {player.hand.hand_name}")
        
        active_players = [p for p in self.game.players if p.is_active and p.hand]
        
        if not active_players:
            self.log_message("\nNo active players!")
            return
        
        if len(active_players) == 1:
            winner = active_players[0]
            winner.chips += self.game.pot
            self.log_message(f"\n{winner.name} wins {self.game.pot} chips (all others folded)")
            self.game.pot = 0
            self.update_display()
            return
        
        # Determine winners
        sorted_hands = sorted([(p.hand, p) for p in active_players], key=lambda x: x[0], reverse=True)
        winner_hand = sorted_hands[0][0]
        
        winners = [
            p for p in active_players
            if p.hand.rank == winner_hand.rank
            and p.hand.tiebreakers == winner_hand.tiebreakers
        ]
        
        # Display ranked hands
        self.log_message("\nHands ranked from best to worst:")
        for i, (hand, player) in enumerate(sorted_hands, 1):
            cards_str = self.format_cards(player.cards)
            self.log_message(f"{i}. {player.name}: {cards_str} - {hand.hand_name}")
        
        # Distribute pot
        pot_per_winner = self.game.pot // len(winners)
        remainder = self.game.pot % len(winners)
        
        self.log_message("\n" + "="*70)
        if len(winners) > 1:
            self.log_message("TIE! Winners:")
            for winner in winners:
                winner.chips += pot_per_winner
                if remainder > 0:
                    winner.chips += 1
                    remainder -= 1
                self.log_message(f"  {winner.name} - {winner.hand.hand_name} - wins {pot_per_winner} chips")
        else:
            winners[0].chips += self.game.pot
            self.log_message(f"WINNER: {winners[0].name}")
            self.log_message(f"Hand: {winners[0].hand.hand_name}")
            self.log_message(f"Wins: {self.game.pot} chips")
        
        self.game.pot = 0
        self.log_message("="*70)
        
        self.update_display()
    
    def handle_early_winner(self):
        """Handle case where only one player remains."""
        active = [p for p in self.game.players if p.is_active]
        if active:
            winner = active[0]
            winner.chips += self.game.pot
            self.log_message(f"\n{winner.name} wins {self.game.pot} chips (all others folded)")
        else:
            self.log_message("All players folded - no winner")
        self.game.pot = 0
        self.update_display()
        self.next_hand_button.config(state=tk.NORMAL)
    
    def next_hand(self):
        """Start the next hand."""
        active_count = sum(1 for p in self.game.players if p.chips > 0)
        if active_count < 2:
            messagebox.showinfo("Game Over", "Not enough players with chips. Game over!")
            return
        
        self.next_hand_button.config(state=tk.DISABLED)
        self.play_hand()
    
    def new_game(self):
        """Start a new game."""
        self.create_startup_screen()


def main():
    """Main function to run the GUI."""
    root = tk.Tk()
    app = PokerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

