"""This is a graphical implementation of 2 player The Eyes Have It using tkinter"""
import tkinter as tk
import random
from tkinter import messagebox
from tehigame_2player import TehiGame
from cardlib_enum import FaceCard, CardSuit

class TehiGameGUI:
    """Graphical user interface for Tehi Game"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("The Eyes Have It - Tehi Game")
        self.root.geometry("1000x750")
        self.root.configure(bg='#2d5016')  # Dark green background
        
        # Initialize game
        self.game = TehiGame()
        
        # Track selected cards for discarding
        self.selected_player_indices = set()
        self.player_card_frames = []
        self.dealer_card_frames = []
        self.discard_phase_active = False
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        
        # Title
        title_label = tk.Label(
            self.root, 
            text="The Eyes Have It", 
            font=('Arial', 24, 'bold'),
            bg='#2d5016',
            fg='white'
        )
        title_label.pack(pady=10)
        
        # Statistics frame
        stats_frame = tk.Frame(self.root, bg='#2d5016')
        stats_frame.pack(pady=5)
        
        self.stats_label = tk.Label(
            stats_frame,
            text=f'Won: {self.game._gameswon} | Total: {self.game._totalgames} | Best: {self.game._besthandscore}',
            font=('Arial', 12),
            bg='#2d5016',
            fg='white'
        )
        self.stats_label.pack()
        
        # Main content frame - horizontal layout
        main_frame = tk.Frame(self.root, bg='#2d5016')
        main_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Left side - Cards
        cards_frame = tk.Frame(main_frame, bg='#2d5016')
        cards_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
        
        # Dealer section
        dealer_frame = tk.Frame(cards_frame, bg='#2d5016')
        dealer_frame.pack(pady=15)
        
        dealer_title = tk.Label(
            dealer_frame,
            text="Dealer",
            font=('Arial', 14, 'bold'),
            bg='#2d5016',
            fg='#ffcccc'
        )
        dealer_title.pack()
        
        self.dealer_cards_frame = tk.Frame(dealer_frame, bg='#2d5016')
        self.dealer_cards_frame.pack(pady=10)
        
        self.dealer_score_label = tk.Label(
            dealer_frame,
            text="Score: --",
            font=('Arial', 12),
            bg='#2d5016',
            fg='white'
        )
        self.dealer_score_label.pack()
        
        # Player section
        player_frame = tk.Frame(cards_frame, bg='#2d5016')
        player_frame.pack(pady=15)
        
        player_title = tk.Label(
            player_frame,
            text="Player (Click cards to select for discard)",
            font=('Arial', 14, 'bold'),
            bg='#2d5016',
            fg='#ccffcc'
        )
        player_title.pack()
        
        self.player_cards_frame = tk.Frame(player_frame, bg='#2d5016')
        self.player_cards_frame.pack(pady=10)
        
        self.player_score_label = tk.Label(
            player_frame,
            text="Score: --",
            font=('Arial', 12),
            bg='#2d5016',
            fg='white'
        )
        self.player_score_label.pack()
        
        # Result label
        self.result_label = tk.Label(
            cards_frame,
            text="",
            font=('Arial', 16, 'bold'),
            bg='#2d5016',
            fg='yellow'
        )
        self.result_label.pack(pady=10)
        
        # Right side - Buttons
        button_panel = tk.Frame(main_frame, bg='#2d5016', width=220)
        button_panel.pack(side=tk.RIGHT, padx=20, fill=tk.Y)
        button_panel.pack_propagate(False)
        
        # Instructions
        instructions = tk.Label(
            button_panel,
            text="Instructions:\n\n1. Click 'Deal Cards'\nto start a round\n\n2. Click player cards\nto select for discard\n\n3. Click 'Discard Selected'\nto discard and draw\n\n4. Click 'Finish Round'\nto determine winner",
            font=('Arial', 10),
            bg='#2d5016',
            fg='white',
            justify=tk.LEFT,
            wraplength=200
        )
        instructions.pack(pady=10)
        
        # Buttons
        self.deal_button = tk.Button(
            button_panel,
            text="Deal Cards",
            command=self.deal_cards,
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            padx=15,
            pady=12,
            relief=tk.RAISED,
            cursor='hand2',
            width=18
        )
        self.deal_button.pack(pady=10)
        
        self.discard_button = tk.Button(
            button_panel,
            text="Discard Selected",
            command=self.discard_cards,
            font=('Arial', 12, 'bold'),
            bg='#FF9800',
            fg='white',
            padx=15,
            pady=12,
            relief=tk.RAISED,
            cursor='hand2',
            width=18,
            state=tk.DISABLED
        )
        self.discard_button.pack(pady=10)
        
        self.finish_button = tk.Button(
            button_panel,
            text="Finish Round",
            command=self.finish_round,
            font=('Arial', 12, 'bold'),
            bg='#9C27B0',
            fg='white',
            padx=15,
            pady=12,
            relief=tk.RAISED,
            cursor='hand2',
            width=18,
            state=tk.DISABLED
        )
        self.finish_button.pack(pady=10)
        
        new_deck_button = tk.Button(
            button_panel,
            text="New Deck",
            command=self.new_deck,
            font=('Arial', 11),
            bg='#2196F3',
            fg='white',
            padx=15,
            pady=10,
            relief=tk.RAISED,
            cursor='hand2',
            width=18
        )
        new_deck_button.pack(pady=10)
        
        quit_button = tk.Button(
            button_panel,
            text="Quit",
            command=self.quit_game,
            font=('Arial', 11),
            bg='#f44336',
            fg='white',
            padx=15,
            pady=10,
            relief=tk.RAISED,
            cursor='hand2',
            width=18
        )
        quit_button.pack(pady=10)
        
        # Initialize with empty hands
        self.clear_hands()
        
    def create_card_widget(self, parent, card, index, is_player):
        """Create a visual representation of a card with click selection"""
        card_frame = tk.Frame(
            parent,
            bg='white',
            relief=tk.RAISED,
            borderwidth=2,
            width=80,
            height=120
        )
        card_frame.pack(side=tk.LEFT, padx=5)
        card_frame.pack_propagate(False)
        
        # Card content
        if isinstance(card, FaceCard):
            rank_text = f"{card.rank.symbol}\n{card.suit.symbol}\n({card.eyes} eyes)"
            color = 'red' if card.suit in [CardSuit.HEARTS, CardSuit.DIAMONDS] else 'black'
        else:
            rank_text = f"{card.rank.symbol}\n{card.suit.symbol}"
            color = 'red' if card.suit in [CardSuit.HEARTS, CardSuit.DIAMONDS] else 'black'
        
        card_label = tk.Label(
            card_frame,
            text=rank_text,
            font=('Arial', 14, 'bold'),
            bg='white',
            fg=color,
            justify=tk.CENTER,
            cursor='hand2'
        )
        card_label.pack(expand=True)
        
        # Make player cards clickable if discard phase is active
        if is_player and self.discard_phase_active:
            def on_click(event=None):
                self.toggle_player_card_selection(index)
            
            card_frame.bind("<Button-1>", on_click)
            card_label.bind("<Button-1>", on_click)
            card_frame.config(cursor='hand2')
        
        return card_frame
    
    def display_hand(self, hand, cards_frame, is_player):
        """Display a hand of cards with selection capability"""
        # Clear existing cards
        for widget in cards_frame.winfo_children():
            widget.destroy()
        
        # Clear card frames list
        if is_player:
            self.player_card_frames.clear()
        else:
            self.dealer_card_frames.clear()
        
        # Display each card
        for idx, card in enumerate(hand._hand):
            frame = self.create_card_widget(cards_frame, card, idx, is_player)
            if is_player:
                self.player_card_frames.append(frame)
            else:
                self.dealer_card_frames.append(frame)
        
        # Update selection highlighting
        self.update_selection_highlighting()
    
    def clear_hands(self):
        """Clear the display of both hands"""
        for widget in self.player_cards_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()
        
        self.player_card_frames.clear()
        self.dealer_card_frames.clear()
        self.selected_player_indices.clear()
        self.discard_phase_active = False
        
        self.player_score_label.config(text="Score: --")
        self.dealer_score_label.config(text="Score: --")
        self.result_label.config(text="")
        
        # Disable buttons
        self.discard_button.config(state=tk.DISABLED)
        self.finish_button.config(state=tk.DISABLED)
    
    def deal_cards(self):
        """Deal cards to start a new round"""
        # Return existing hands to deck
        self.game._playerhand.return_to_deck(self.game._deck)
        self.game._dealerhand.return_to_deck(self.game._deck)
        
        # Shuffle and deal
        self.game._deck.shuffle()
        self.game._playerhand.deal(self.game._deck)
        self.game._dealerhand.deal(self.game._deck)
        
        # Increment total games
        self.game._totalgames += 1
        
        # Reset selections
        self.selected_player_indices.clear()
        self.discard_phase_active = True
        
        # Display hands
        self.display_hand(self.game._playerhand, self.player_cards_frame, is_player=True)
        self.display_hand(self.game._dealerhand, self.dealer_cards_frame, is_player=False)
        
        # Display scores
        self.update_scores()
        
        # Clear result
        self.result_label.config(text="Select cards to discard, then click Discard Selected", fg='lightblue')
        
        # Enable discard and finish buttons
        self.discard_button.config(state=tk.NORMAL)
        self.finish_button.config(state=tk.NORMAL)
        
        # Update statistics
        self.update_statistics()
    
    def toggle_player_card_selection(self, idx):
        """Toggle selection of a player card for discarding"""
        if not self.discard_phase_active:
            return
        
        if idx in self.selected_player_indices:
            self.selected_player_indices.remove(idx)
        else:
            self.selected_player_indices.add(idx)
        
        self.update_selection_highlighting()
    
    def update_selection_highlighting(self):
        """Update the visual highlighting of selected cards"""
        # Update player cards
        for idx, frame in enumerate(self.player_card_frames):
            if idx in self.selected_player_indices:
                frame.config(highlightthickness=4, highlightbackground='#FF6B6B', highlightcolor='#FF6B6B')
            else:
                frame.config(highlightthickness=0)
    
    def discard_cards(self):
        """Discard selected player cards and auto-discard dealer cards, then draw new ones"""
        if not self.discard_phase_active:
            messagebox.showinfo("Discard Cards", "Please deal cards first.")
            return
        
        # Discard player cards
        player_hand = self.game._playerhand._hand
        if self.selected_player_indices:
            # Sort indices in reverse to avoid index shifting issues
            indices_to_remove = sorted(self.selected_player_indices, reverse=True)
            for idx in indices_to_remove:
                card = player_hand.pop(idx)
                self.game._deck.add(card)
        
        # Auto-discard dealer cards (discard lowest scoring cards)
        dealer_hand = self.game._dealerhand._hand
        dealer_indices_to_remove = []
        if len(dealer_hand) > 0:
            # Calculate contribution of each card to the score
            # For simplicity, discard 1-2 cards with lowest individual value
            # We'll discard cards that contribute least to the score
            card_values = []
            for idx, card in enumerate(dealer_hand):
                if isinstance(card, FaceCard):
                    # Face cards contribute eyes, but we want to keep high eye cards
                    # So we'll value them by eyes (higher is better)
                    value = card.eyes * 10  # Weight eyes more
                else:
                    # Regular cards contribute their rank value
                    value = card.value
                card_values.append(value)
            
            # Find indices of cards with lowest values
            sorted_indices = sorted(range(len(card_values)), key=lambda i: card_values[i])
            # Discard 1-2 lowest cards (randomly choose 1 or 2)
            num_to_discard = random.randint(1, min(2, len(dealer_hand)))
            dealer_indices_to_remove = sorted_indices[:num_to_discard]
            
            # Remove dealer cards in reverse order
            for idx in sorted(dealer_indices_to_remove, reverse=True):
                card = dealer_hand.pop(idx)
                self.game._deck.add(card)
        
        # Draw new cards for player
        num_player_discarded = len(self.selected_player_indices)
        for _ in range(num_player_discarded):
            if len(self.game._deck) > 0:
                card = self.game._deck.deal()
                card.faceup = True
                player_hand.append(card)
        
        # Draw new cards for dealer
        num_dealer_discarded = len(dealer_indices_to_remove)
        for _ in range(num_dealer_discarded):
            if len(self.game._deck) > 0:
                card = self.game._deck.deal()
                card.faceup = True
                dealer_hand.append(card)
        
        # Clear selections
        self.selected_player_indices.clear()
        
        # Refresh display
        self.display_hand(self.game._playerhand, self.player_cards_frame, is_player=True)
        self.display_hand(self.game._dealerhand, self.dealer_cards_frame, is_player=False)
        
        # Update scores
        self.update_scores()
        
        # Update best hand score
        self.game._besthandscore = max(self.game._besthandscore, self.game._playerhand.score)
        self.update_statistics()
        
        # Disable discard button after discarding
        self.discard_phase_active = False
        self.discard_button.config(state=tk.DISABLED)
        self.result_label.config(text="Cards discarded! Click Finish Round to determine winner.", fg='lightgreen')
    
    def update_scores(self):
        """Update the score displays"""
        player_score = self.game._playerhand.score
        dealer_score = self.game._dealerhand.score
        
        self.player_score_label.config(text=f"Score: {player_score}")
        self.dealer_score_label.config(text=f"Score: {dealer_score}")
    
    def finish_round(self):
        """Finish the round and determine the winner"""
        # If discard phase is still active, allow finishing without discarding
        # (player can choose to skip discarding)
        if self.discard_phase_active:
            # Auto-discard dealer cards even if player skips
            dealer_hand = self.game._dealerhand._hand
            if len(dealer_hand) > 0:
                card_values = []
                for idx, card in enumerate(dealer_hand):
                    if isinstance(card, FaceCard):
                        value = card.eyes * 10
                    else:
                        value = card.value
                    card_values.append(value)
                
                sorted_indices = sorted(range(len(card_values)), key=lambda i: card_values[i])
                num_to_discard = random.randint(1, min(2, len(dealer_hand)))
                dealer_indices_to_remove = sorted_indices[:num_to_discard]
                
                for idx in sorted(dealer_indices_to_remove, reverse=True):
                    card = dealer_hand.pop(idx)
                    self.game._deck.add(card)
                
                # Draw new cards for dealer
                for _ in range(len(dealer_indices_to_remove)):
                    if len(self.game._deck) > 0:
                        card = self.game._deck.deal()
                        card.faceup = True
                        dealer_hand.append(card)
                
                # Refresh display
                self.display_hand(self.game._dealerhand, self.dealer_cards_frame, is_player=False)
                self.update_scores()
            
            self.discard_phase_active = False
        
        # Update best hand score
        self.game._besthandscore = max(self.game._besthandscore, self.game._playerhand.score)
        
        # Determine winner
        if self.game._dealerhand > self.game._playerhand:
            result_text = "Dealer Wins!!"
            result_color = '#ffcccc'
        elif self.game._dealerhand < self.game._playerhand:
            result_text = "Player Wins!!"
            result_color = '#ccffcc'
            self.game._gameswon += 1
        else:
            result_text = "TIE!!"
            result_color = 'yellow'
        
        self.result_label.config(text=result_text, fg=result_color)
        
        # Round is now complete
        self.discard_phase_active = False
        self.selected_player_indices.clear()
        
        # Disable buttons
        self.discard_button.config(state=tk.DISABLED)
        self.finish_button.config(state=tk.DISABLED)
        
        # Update statistics
        self.update_statistics()
        
    def new_deck(self):
        """Start a new game with a fresh deck"""
        self.game = TehiGame()
        self.clear_hands()
        self.update_statistics()
        self.result_label.config(text="New deck created!", fg='lightblue')
        
    def update_statistics(self):
        """Update the statistics display"""
        self.stats_label.config(
            text=f'Won: {self.game._gameswon} | Total: {self.game._totalgames} | Best: {self.game._besthandscore}'
        )
    
    def quit_game(self):
        """Quit the game"""
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TehiGameGUI(root)
    root.mainloop()

