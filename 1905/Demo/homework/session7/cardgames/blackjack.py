"""
Blackjack game implementation using cardlib_enum
Supports 1-4 players playing multiple hands with option to use new deck or quit
"""
from __future__ import annotations
from cardlib_enum import CardDeck, CardRank, PlayingCard
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class HandResult:
    """Result of a player's hand"""
    player_name: str
    hand: List[PlayingCard]
    value: int
    is_blackjack: bool
    is_bust: bool
    bet: int
    winnings: int = 0


class BlackjackHand:
    """Represents a blackjack hand with value calculation"""
    
    BLACKJACK_VALUE = 21
    DEALER_STAND_VALUE = 17
    
    def __init__(self, cards: List[PlayingCard] = None):
        self.cards = cards or []
    
    def add_card(self, card: PlayingCard) -> None:
        """Add a card to the hand"""
        self.cards.append(card)
    
    def calculate_value(self) -> int:
        """Calculate the best possible value of the hand (Ace = 1 or 11)"""
        total = 0
        aces = 0
        
        for card in self.cards:
            rank_value = card.rank.value
            if rank_value == 1:  # Ace
                aces += 1
                total += 11
            elif rank_value >= 11:  # Face cards (J, Q, K)
                total += 10
            else:
                total += rank_value
        
        # Adjust for Aces: if total > 21, treat Aces as 1 instead of 11
        while total > self.BLACKJACK_VALUE and aces > 0:
            total -= 10
            aces -= 1
        
        return total
    
    def is_blackjack(self) -> bool:
        """Check if hand is a blackjack (Ace + 10-value card, exactly 2 cards)"""
        if len(self.cards) != 2:
            return False
        value = self.calculate_value()
        return value == self.BLACKJACK_VALUE
    
    def is_bust(self) -> bool:
        """Check if hand is bust (over 21)"""
        return self.calculate_value() > self.BLACKJACK_VALUE
    
    def __str__(self) -> str:
        """String representation of the hand"""
        cards_str = " ".join(str(card) for card in self.cards)
        value = self.calculate_value()
        status = ""
        if self.is_blackjack():
            status = " (BLACKJACK!)"
        elif self.is_bust():
            status = " (BUST)"
        return f"{cards_str} - Value: {value}{status}"


class Player:
    """Represents a blackjack player"""
    
    def __init__(self, name: str, starting_chips: int = 1000):
        self.name = name
        self._chips = starting_chips
        self.hand = BlackjackHand()
        self.bet = 0
        self.stand = False
        self.busted = False
        self.blackjack = False
    
    @property
    def chips(self) -> int:
        """Get player's chips"""
        return self._chips
    
    @chips.setter
    def chips(self, value: int) -> None:
        """Set player's chips"""
        self._chips = max(0, value)
    
    def place_bet(self, amount: int) -> bool:
        """Place a bet. Returns True if successful"""
        if amount > self._chips:
            return False
        if amount <= 0:
            return False
        self.bet = amount
        self._chips -= amount
        return True
    
    def win(self, amount: int) -> None:
        """Add winnings to player's chips"""
        self._chips += amount
    
    def reset_hand(self) -> None:
        """Reset hand for new round"""
        self.hand = BlackjackHand()
        self.bet = 0
        self.stand = False
        self.busted = False
        self.blackjack = False
    
    def can_play(self) -> bool:
        """Check if player can still play (hasn't stood or busted)"""
        return not self.stand and not self.busted
    
    def __str__(self) -> str:
        """String representation of player"""
        return f"{self.name}: {self.chips} chips"


class Dealer:
    """Represents the dealer"""
    
    def __init__(self):
        self.hand = BlackjackHand()
        self.busted = False
        self.blackjack = False
    
    def reset_hand(self) -> None:
        """Reset hand for new round"""
        self.hand = BlackjackHand()
        self.busted = False
        self.blackjack = False
    
    def should_hit(self) -> bool:
        """Dealer must hit on 16 or less, stand on 17 or more"""
        value = self.hand.calculate_value()
        return value < BlackjackHand.DEALER_STAND_VALUE


class BlackjackGame:
    """Main blackjack game manager"""
    
    MIN_PLAYERS = 1
    MAX_PLAYERS = 4
    DEFAULT_STARTING_CHIPS = 1000
    MIN_BET = 5
    BLACKJACK_PAYOUT = 1.5  # 3:2 payout
    
    def __init__(self, num_players: int, starting_chips: int = DEFAULT_STARTING_CHIPS):
        if not (self.MIN_PLAYERS <= num_players <= self.MAX_PLAYERS):
            raise ValueError(f"Number of players must be between {self.MIN_PLAYERS} and {self.MAX_PLAYERS}")
        
        self.num_players = num_players
        self.starting_chips = starting_chips
        self.deck = CardDeck()
        self.deck.shuffle()
        self.players: List[Player] = []
        self.dealer = Dealer()
        self.round_number = 0
        
        self._initialize_players()
    
    def _initialize_players(self) -> None:
        """Initialize players"""
        for i in range(self.num_players):
            name = f"Player {i+1}"
            self.players.append(Player(name, self.starting_chips))
    
    def _get_bet_from_player(self, player: Player) -> int:
        """Get bet amount from player"""
        while True:
            try:
                bet_input = input(f"{player.name}, enter your bet (min {self.MIN_BET}, max {player.chips}, or 'q' to quit): ").strip()
                
                if bet_input.lower() in ('q', 'quit'):
                    return -1  # Signal to quit
                
                bet = int(bet_input)
                
                if bet < self.MIN_BET:
                    print(f"Minimum bet is {self.MIN_BET}")
                    continue
                
                if bet > player.chips:
                    print(f"You only have {player.chips} chips")
                    continue
                
                return bet
            except ValueError:
                print("Please enter a valid number or 'q' to quit")
    
    def _deal_initial_cards(self) -> None:
        """Deal initial two cards to each player and dealer"""
        # Deal first card to all players
        for player in self.players:
            if player.bet > 0:  # Only deal to players who placed bets
                card = self.deck.deal()
                card.faceup = True
                player.hand.add_card(card)
        
        # Deal first card to dealer
        dealer_card = self.deck.deal()
        dealer_card.faceup = True
        self.dealer.hand.add_card(dealer_card)
        
        # Deal second card to all players
        for player in self.players:
            if player.bet > 0:
                card = self.deck.deal()
                card.faceup = True
                player.hand.add_card(card)
                # Check for blackjack
                if player.hand.is_blackjack():
                    player.blackjack = True
                    player.stand = True
        
        # Deal second card to dealer (face down initially)
        dealer_card2 = self.deck.deal()
        dealer_card2.faceup = False
        self.dealer.hand.add_card(dealer_card2)
        
        # Check dealer blackjack
        if self.dealer.hand.is_blackjack():
            self.dealer.blackjack = True
            # Show dealer's second card
            dealer_card2.faceup = True
    
    def _display_game_state(self, show_dealer_hole: bool = False) -> None:
        """Display current game state"""
        print("\n" + "="*70)
        print("CURRENT GAME STATE")
        print("="*70)
        
        # Show dealer's hand
        if show_dealer_hole:
            dealer_cards = " ".join(str(card) for card in self.dealer.hand.cards)
            dealer_value = self.dealer.hand.calculate_value()
            dealer_status = ""
            if self.dealer.blackjack:
                dealer_status = " (BLACKJACK!)"
            elif self.dealer.busted:
                dealer_status = " (BUST)"
            print(f"Dealer: {dealer_cards} - Value: {dealer_value}{dealer_status}")
        else:
            # Show first card, hide second
            visible_card = str(self.dealer.hand.cards[0]) if self.dealer.hand.cards else "XX"
            print(f"Dealer: {visible_card} XX")
        
        # Show players' hands
        print("\nPlayers:")
        for player in self.players:
            if player.bet > 0:
                status = ""
                if player.blackjack:
                    status = " (BLACKJACK!)"
                elif player.busted:
                    status = " (BUST)"
                elif player.stand:
                    status = " (STAND)"
                print(f"{player.name} (bet: {player.bet}): {player.hand}")
            else:
                print(f"{player.name}: No bet placed")
        
        print("="*70 + "\n")
    
    def _player_turn(self, player: Player) -> bool:
        """Handle a player's turn. Returns True if player wants to continue, False to quit"""
        if not player.can_play():
            return True
        
        print(f"\n{player.name}'s turn")
        print(f"Your hand: {player.hand}")
        print(f"Your chips: {player.chips}")
        
        while player.can_play():
            action = input("Choose action: [h]it, [s]tand, or [q]uit: ").strip().lower()
            
            if action in ('q', 'quit'):
                return False
            
            elif action in ('h', 'hit'):
                # Deal a card
                card = self.deck.deal()
                card.faceup = True
                player.hand.add_card(card)
                
                print(f"You drew: {card}")
                print(f"Your hand: {player.hand}")
                
                if player.hand.is_bust():
                    player.busted = True
                    print(f"{player.name} BUSTS!")
                    break
                elif player.hand.is_blackjack() and len(player.hand.cards) == 2:
                    player.blackjack = True
                    player.stand = True
                    print(f"{player.name} has BLACKJACK!")
                    break
            
            elif action in ('s', 'stand'):
                player.stand = True
                print(f"{player.name} stands")
                break
            else:
                print("Invalid choice. Please enter 'h' for hit, 's' for stand, or 'q' to quit")
        
        return True
    
    def _dealer_turn(self) -> None:
        """Handle dealer's turn"""
        # Show dealer's hole card
        if len(self.dealer.hand.cards) > 1:
            self.dealer.hand.cards[1].faceup = True
        
        print("\nDealer's turn")
        print(f"Dealer's hand: {self.dealer.hand}")
        
        # Check for dealer blackjack
        if self.dealer.hand.is_blackjack():
            self.dealer.blackjack = True
            print("Dealer has BLACKJACK!")
            return
        
        # Dealer hits until 17 or more
        while self.dealer.should_hit():
            card = self.deck.deal()
            card.faceup = True
            self.dealer.hand.add_card(card)
            print(f"Dealer draws: {card}")
            print(f"Dealer's hand: {self.dealer.hand}")
            
            if self.dealer.hand.is_bust():
                self.dealer.busted = True
                print("Dealer BUSTS!")
                break
        
        if not self.dealer.busted:
            print("Dealer stands")
    
    def _calculate_winnings(self, player: Player) -> int:
        """Calculate winnings for a player"""
        if player.busted:
            return 0
        
        dealer_value = self.dealer.hand.calculate_value()
        player_value = player.hand.calculate_value()
        
        # Dealer busted - all non-busted players win
        if self.dealer.busted:
            if player.blackjack:
                return int(player.bet * (1 + self.BLACKJACK_PAYOUT))
            return player.bet * 2
        
        # Player blackjack beats dealer non-blackjack
        if player.blackjack and not self.dealer.blackjack:
            return int(player.bet * (1 + self.BLACKJACK_PAYOUT))
        
        # Dealer blackjack beats player non-blackjack
        if self.dealer.blackjack and not player.blackjack:
            return 0
        
        # Both have blackjack - push
        if player.blackjack and self.dealer.blackjack:
            return player.bet
        
        # Compare values
        if player_value > dealer_value:
            if player.blackjack:
                return int(player.bet * (1 + self.BLACKJACK_PAYOUT))
            return player.bet * 2
        elif player_value < dealer_value:
            return 0
        else:
            # Push (tie)
            return player.bet
    
    def _resolve_round(self) -> None:
        """Resolve the round and distribute winnings"""
        print("\n" + "="*70)
        print("ROUND RESULTS")
        print("="*70)
        
        self._display_game_state(show_dealer_hole=True)
        
        dealer_value = self.dealer.hand.calculate_value()
        print(f"\nDealer's final value: {dealer_value}")
        if self.dealer.busted:
            print("Dealer BUSTED - All remaining players win!")
        elif self.dealer.blackjack:
            print("Dealer has BLACKJACK!")
        
        print("\nPlayer Results:")
        for player in self.players:
            if player.bet == 0:
                continue
            
            winnings = self._calculate_winnings(player)
            player.win(winnings)
            net = winnings - player.bet
            
            result = ""
            if player.busted:
                result = "BUST - Lost"
            elif player.blackjack and not self.dealer.blackjack:
                result = "BLACKJACK - Won"
            elif self.dealer.busted:
                result = "Won (Dealer busted)"
            elif player.hand.calculate_value() > dealer_value:
                result = "Won"
            elif player.hand.calculate_value() < dealer_value:
                result = "Lost"
            else:
                result = "Push (Tie)"
            
            print(f"{player.name}: {result}")
            print(f"  Bet: {player.bet}, Winnings: {winnings}, Net: {net:+d}")
            print(f"  New chip count: {player.chips}")
        
        print("="*70 + "\n")
    
    def _collect_bets(self) -> bool:
        """Collect bets from all players. Returns False if any player wants to quit"""
        print("\n" + "="*70)
        print(f"ROUND {self.round_number + 1} - PLACE YOUR BETS")
        print("="*70)
        
        active_players = [p for p in self.players if p.chips >= self.MIN_BET]
        
        if not active_players:
            print("No players have enough chips to play!")
            return False
        
        print(f"\nActive players: {', '.join(p.name for p in active_players)}")
        print(f"Minimum bet: {self.MIN_BET}")
        
        for player in self.players:
            if player.chips < self.MIN_BET:
                print(f"{player.name} doesn't have enough chips to play (need {self.MIN_BET}, have {player.chips})")
                continue
            
            bet = self._get_bet_from_player(player)
            if bet == -1:
                return False  # Player wants to quit
            
            player.place_bet(bet)
            print(f"{player.name} bets {bet} chips")
        
        return True
    
    def _reset_for_new_round(self) -> None:
        """Reset all hands for a new round"""
        for player in self.players:
            player.reset_hand()
        self.dealer.reset_hand()
    
    def _check_deck_size(self) -> bool:
        """Check if deck has enough cards. Returns True if OK, False if needs new deck"""
        # Need at least 10 cards per player + dealer (safety margin)
        cards_needed = (self.num_players + 1) * 10
        return len(self.deck) >= cards_needed
    
    def play_round(self) -> bool:
        """Play a single round. Returns True to continue, False to quit"""
        self.round_number += 1
        
        # Reset hands
        self._reset_for_new_round()
        
        # Collect bets
        if not self._collect_bets():
            return False
        
        # Check if any players placed bets
        if not any(p.bet > 0 for p in self.players):
            print("No bets placed. Round cancelled.")
            return True
        
        # Deal initial cards
        self._deal_initial_cards()
        self._display_game_state(show_dealer_hole=False)
        
        # Check for dealer blackjack
        if self.dealer.blackjack:
            print("Dealer has BLACKJACK!")
            self._resolve_round()
            return True
        
        # Player turns
        for player in self.players:
            if player.bet > 0 and not player.blackjack:
                if not self._player_turn(player):
                    return False  # Player wants to quit
                self._display_game_state(show_dealer_hole=False)
        
        # Dealer turn (only if at least one player hasn't busted)
        if any(p.bet > 0 and not p.busted for p in self.players):
            self._dealer_turn()
        
        # Resolve round
        self._resolve_round()
        
        return True
    
    def display_status(self) -> None:
        """Display current game status"""
        print("\n" + "="*70)
        print("GAME STATUS")
        print("="*70)
        print(f"Round: {self.round_number}")
        print(f"Cards remaining in deck: {len(self.deck)}")
        print("\nPlayer Status:")
        for player in self.players:
            print(f"  {player}")
        print("="*70 + "\n")
    
    def use_new_deck(self) -> None:
        """Create and shuffle a new deck"""
        self.deck = CardDeck()
        self.deck.shuffle()
        print("New deck created and shuffled!")


def get_user_input(prompt: str, validator, error_msg: str, default: Optional[int] = None) -> Optional[int]:
    """Get and validate user input"""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and default is not None:
                return default
            if not user_input:
                print("Please enter a value.")
                continue
            value = int(user_input)
            if validator(value):
                return value
            print(error_msg)
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the game"""
    print("="*70)
    print("WELCOME TO BLACKJACK!")
    print("="*70)
    print("\nRules:")
    print("- Goal: Get as close to 21 as possible without going over")
    print("- Face cards (J, Q, K) are worth 10")
    print("- Ace can be 1 or 11 (whichever is better)")
    print("- Blackjack (Ace + 10-value card) pays 3:2")
    print("- Dealer must hit until 17 or more")
    print("- Ties push (bet returned)")
    print("="*70)
    
    num_players = get_user_input(
        "Enter number of players (1-4): ",
        lambda x: 1 <= x <= 4,
        "Please enter a number between 1 and 4."
    )
    
    starting_chips = get_user_input(
        "Enter starting chips per player (default 1000): ",
        lambda x: x > 0,
        "Starting chips must be positive.",
        default=BlackjackGame.DEFAULT_STARTING_CHIPS
    ) or BlackjackGame.DEFAULT_STARTING_CHIPS
    
    game = BlackjackGame(num_players, starting_chips)
    
    print("\nGame started!")
    game.display_status()
    
    while True:
        # Play a round
        if not game.play_round():
            print("Game ended by player request.")
            break
        
        # Check if players can continue
        active_players = [p for p in game.players if p.chips >= game.MIN_BET]
        if not active_players:
            print("\nNo players have enough chips to continue playing!")
            break
        
        # Check deck size
        if not game._check_deck_size():
            print(f"\nWarning: Only {len(game.deck)} cards remaining in deck.")
        
        # Ask what to do next
        while True:
            print("\nOptions:")
            print("  [c]ontinue - Play another round with current deck")
            print("  [n]ew deck - Get a new deck and continue")
            print("  [q]uit - End the game")
            
            choice = input("Your choice: ").strip().lower()
            
            if choice in ('c', 'continue'):
                break
            elif choice in ('n', 'new deck', 'new'):
                game.use_new_deck()
                break
            elif choice in ('q', 'quit'):
                print("\nThanks for playing!")
                game.display_status()
                return
            else:
                print("Invalid choice. Please enter 'c', 'n', or 'q'.")
    
    print("\nGame Over!")
    game.display_status()


if __name__ == "__main__":
    main()

