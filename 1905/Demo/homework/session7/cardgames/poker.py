"""
Poker game implementation using cardlib_enum
Supports 1-4 players playing 5-card draw poker with betting

Refactored for better maintainability, pythonic code, and OOP principles.
"""
from __future__ import annotations
from cardlib_enum import CardDeck, CardRank, PlayingCard
from typing import List, Tuple, Optional, Protocol
from collections import Counter
from enum import IntEnum
from dataclasses import dataclass


class HandRank(IntEnum):
    """Poker hand rankings (higher number = better hand)"""
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


HAND_NAMES = {
    HandRank.HIGH_CARD: "High Card",
    HandRank.ONE_PAIR: "One Pair",
    HandRank.TWO_PAIR: "Two Pair",
    HandRank.THREE_OF_A_KIND: "Three of a Kind",
    HandRank.STRAIGHT: "Straight",
    HandRank.FLUSH: "Flush",
    HandRank.FULL_HOUSE: "Full House",
    HandRank.FOUR_OF_A_KIND: "Four of a Kind",
    HandRank.STRAIGHT_FLUSH: "Straight Flush",
    HandRank.ROYAL_FLUSH: "Royal Flush"
}


@dataclass
class HandEvaluation:
    """Result of evaluating a poker hand"""
    rank: HandRank
    tiebreakers: List[int]


class PokerHand:
    """Represents a poker hand and evaluates its rank"""
    
    CARDS_IN_HAND = 5
    WHEEL_RANKS = [1, 2, 3, 4, 5]
    
    def __init__(self, name: str, cards: List[PlayingCard]):
        if len(cards) != self.CARDS_IN_HAND:
            raise ValueError(f"Poker hand must have exactly {self.CARDS_IN_HAND} cards")
        self.name = name
        self.cards = sorted(cards, key=lambda c: c.rank.value)
        self._evaluation = self._evaluate_hand()
        self.rank = self._evaluation.rank
        self.tiebreakers = self._evaluation.tiebreakers
    
    def _evaluate_hand(self) -> HandEvaluation:
        """Evaluate the poker hand and return evaluation result"""
        ranks = [card.rank.value for card in self.cards]
        suits = [card.suit for card in self.cards]
        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)
        
        is_flush = len(suit_counts) == 1
        is_straight, sorted_ranks = self._check_straight(ranks)
        
        # Check hand types from highest to lowest
        if is_flush and is_straight:
            return self._evaluate_straight_flush(sorted_ranks)
        
        if 4 in rank_counts.values():
            return self._evaluate_four_of_a_kind(rank_counts)
        
        if 3 in rank_counts.values() and 2 in rank_counts.values():
            return self._evaluate_full_house(rank_counts)
        
        if is_flush:
            return HandEvaluation(HandRank.FLUSH, sorted(ranks, reverse=True))
        
        if is_straight:
            high_card = 5 if sorted_ranks == self.WHEEL_RANKS else sorted_ranks[-1]
            return HandEvaluation(HandRank.STRAIGHT, [high_card])
        
        if 3 in rank_counts.values():
            return self._evaluate_three_of_a_kind(rank_counts)
        
        pairs = sorted([r for r, count in rank_counts.items() if count == 2], reverse=True)
        if len(pairs) == 2:
            return self._evaluate_two_pair(rank_counts, pairs)
        
        if 2 in rank_counts.values():
            return self._evaluate_one_pair(rank_counts)
        
        return HandEvaluation(HandRank.HIGH_CARD, sorted(ranks, reverse=True))
    
    def _check_straight(self, ranks: List[int]) -> Tuple[bool, List[int]]:
        """Check if ranks form a straight"""
        sorted_ranks = sorted(set(ranks))
        if len(sorted_ranks) != self.CARDS_IN_HAND:
            return False, sorted_ranks
        
        is_regular_straight = sorted_ranks[-1] - sorted_ranks[0] == 4
        is_wheel = sorted_ranks == self.WHEEL_RANKS
        
        return (is_regular_straight or is_wheel), sorted_ranks
    
    def _evaluate_straight_flush(self, sorted_ranks: List[int]) -> HandEvaluation:
        """Evaluate straight flush or royal flush"""
        if sorted_ranks[-1] == 13:  # A-K-Q-J-10
            return HandEvaluation(HandRank.ROYAL_FLUSH, [])
        
        high_card = 5 if sorted_ranks == self.WHEEL_RANKS else sorted_ranks[-1]
        return HandEvaluation(HandRank.STRAIGHT_FLUSH, [high_card])
    
    def _evaluate_four_of_a_kind(self, rank_counts: Counter) -> HandEvaluation:
        """Evaluate four of a kind"""
        four_kind = next(r for r, count in rank_counts.items() if count == 4)
        kicker = next(r for r, count in rank_counts.items() if count == 1)
        return HandEvaluation(HandRank.FOUR_OF_A_KIND, [four_kind, kicker])
    
    def _evaluate_full_house(self, rank_counts: Counter) -> HandEvaluation:
        """Evaluate full house"""
        three_kind = next(r for r, count in rank_counts.items() if count == 3)
        pair = next(r for r, count in rank_counts.items() if count == 2)
        return HandEvaluation(HandRank.FULL_HOUSE, [three_kind, pair])
    
    def _evaluate_three_of_a_kind(self, rank_counts: Counter) -> HandEvaluation:
        """Evaluate three of a kind"""
        three_kind = next(r for r, count in rank_counts.items() if count == 3)
        kickers = sorted([r for r, count in rank_counts.items() if count == 1], reverse=True)
        return HandEvaluation(HandRank.THREE_OF_A_KIND, [three_kind] + kickers)
    
    def _evaluate_two_pair(self, rank_counts: Counter, pairs: List[int]) -> HandEvaluation:
        """Evaluate two pair"""
        kicker = next(r for r, count in rank_counts.items() if count == 1)
        return HandEvaluation(HandRank.TWO_PAIR, pairs + [kicker])
    
    def _evaluate_one_pair(self, rank_counts: Counter) -> HandEvaluation:
        """Evaluate one pair"""
        pair = next(r for r, count in rank_counts.items() if count == 2)
        kickers = sorted([r for r, count in rank_counts.items() if count == 1], reverse=True)
        return HandEvaluation(HandRank.ONE_PAIR, [pair] + kickers)
    
    @property
    def hand_name(self) -> str:
        """Get the name of the hand rank"""
        return HAND_NAMES[self.rank]
    
    def __str__(self) -> str:
        """String representation of the hand"""
        cards_str = " ".join(str(card) for card in self.cards)
        return f"{self.name}: {cards_str} - {self.hand_name}"
    
    def __lt__(self, other: PokerHand) -> bool:
        """Compare two hands (for sorting)"""
        if self.rank != other.rank:
            return self.rank < other.rank
        
        for self_tb, other_tb in zip(self.tiebreakers, other.tiebreakers):
            if self_tb != other_tb:
                return self_tb < other_tb
        return False
    
    def __eq__(self, other: PokerHand) -> bool:
        """Check if two hands are equal"""
        return self.rank == other.rank and self.tiebreakers == other.tiebreakers


class PlayerStrategy(Protocol):
    """Protocol for player strategies (human or AI)"""
    def get_betting_action(self, player: 'Player', current_bet: int) -> str: ...
    def get_discard_decision(self, player: 'Player') -> List[int]: ...


class HumanPlayerStrategy:
    """Strategy for human player input"""
    
    @staticmethod
    def get_betting_action(player: 'Player', current_bet: int) -> str:
        """Get betting action from human player"""
        call_amount = current_bet - player.current_bet
        max_raise = min(player.chips - call_amount, player.chips)
        
        while True:
            prompt = ("\nOptions: [f]old, [c]heck, [r]aise <amount>" 
                     if call_amount == 0 
                     else f"\nOptions: [f]old, [c]all ({call_amount}), [r]aise <amount>")
            print(prompt)
            
            choice = input("Your action: ").strip().lower()
            
            if choice in ('f', 'fold'):
                return "fold"
            elif choice in ('c', 'call', 'check'):
                return "call"
            elif choice.startswith(('r', 'raise')):
                try:
                    parts = choice.split()
                    raise_amt = int(parts[1]) if len(parts) > 1 else int(input("Enter raise amount: "))
                    
                    if raise_amt < 0:
                        print("Raise amount must be positive")
                        continue
                    
                    if call_amount + raise_amt > player.chips:
                        print(f"Not enough chips. Maximum raise: {max_raise}")
                        continue
                    
                    return f"raise {raise_amt}"
                except ValueError:
                    print("Invalid raise amount")
                    continue
            else:
                print("Invalid choice. Please try again.")
    
    @staticmethod
    def get_discard_decision(player: 'Player') -> List[int]:
        """Get discard decision from human player"""
        while True:
            discard_input = input(
                "Enter card positions to discard (1-5, comma-separated, or 'none'): "
            ).strip().lower()
            
            if discard_input in ('none', ''):
                return []
            
            try:
                positions = [int(x.strip()) - 1 for x in discard_input.split(',')]
                discard_indices = [p for p in positions if 0 <= p < 5]
                
                if len(discard_indices) != len(set(discard_indices)):
                    print("Duplicate positions not allowed")
                    continue
                
                if len(discard_indices) > 3:
                    print("Can discard at most 3 cards")
                    continue
                
                return sorted(discard_indices, reverse=True)
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")


class AIPlayerStrategy:
    """Strategy for AI player decisions"""
    
    STRONG_HAND_THRESHOLD = HandRank.THREE_OF_A_KIND
    MEDIUM_HAND_THRESHOLD = HandRank.ONE_PAIR
    MAX_DISCARD_COUNT = 3
    
    @staticmethod
    def get_betting_action(player: 'Player', current_bet: int) -> str:
        """Get betting action from AI player"""
        call_amount = current_bet - player.current_bet
        hand_strength = player.hand.rank if player.hand else HandRank.HIGH_CARD
        
        if hand_strength >= AIPlayerStrategy.STRONG_HAND_THRESHOLD:
            if call_amount == 0:
                raise_amt = min(50, player.chips // 4)
                return f"raise {raise_amt}" if raise_amt > 0 else "call"
            return "call" if call_amount <= player.chips // 2 else "fold"
        
        elif hand_strength >= AIPlayerStrategy.MEDIUM_HAND_THRESHOLD:
            if call_amount == 0 or call_amount <= player.chips // 4:
                return "call"
            return "fold"
        
        else:
            return "call" if call_amount == 0 else "fold"
    
    @staticmethod
    def get_discard_decision(player: 'Player') -> List[int]:
        """Get discard decision from AI player"""
        if not player.hand:
            return []
        
        hand_strength = player.hand.rank
        
        if hand_strength >= HandRank.THREE_OF_A_KIND:
            return []  # Keep strong hands
        elif hand_strength == HandRank.TWO_PAIR:
            return [4]  # Discard the kicker (last card)
        elif hand_strength == HandRank.ONE_PAIR:
            return [4, 3, 2]  # Discard three non-pair cards
        else:
            return [4, 3, 2]  # Discard three cards, keep two highest


class Player:
    """Represents a player with chips, hand, and betting state"""
    
    def __init__(self, name: str, starting_chips: int = 1000, strategy: Optional[PlayerStrategy] = None):
        self.name = name
        self._chips = starting_chips
        self.current_bet = 0
        self.total_bet_this_round = 0
        self.folded = False
        self.all_in = False
        self.hand: Optional[PokerHand] = None
        self.cards: List[PlayingCard] = []
        self.strategy = strategy or AIPlayerStrategy()
    
    @property
    def chips(self) -> int:
        """Get player's chips"""
        return self._chips
    
    @chips.setter
    def chips(self, value: int) -> None:
        """Set player's chips and update all-in status"""
        self._chips = max(0, value)
        if self._chips == 0:
            self.all_in = True
    
    @property
    def is_active(self) -> bool:
        """Check if player is still active (not folded)"""
        return not self.folded
    
    @property
    def can_bet(self) -> bool:
        """Check if player can place bets"""
        return self.is_active and not self.all_in
    
    def bet(self, amount: int) -> int:
        """Place a bet. Returns actual amount bet (may be less if all-in)"""
        if not self.can_bet:
            return 0
        
        actual_bet = min(amount, self._chips)
        self._chips -= actual_bet
        self.current_bet += actual_bet
        self.total_bet_this_round += actual_bet
        
        if self._chips == 0:
            self.all_in = True
        
        return actual_bet
    
    def fold(self) -> None:
        """Player folds"""
        self.folded = True
    
    def reset_betting_state(self) -> None:
        """Reset betting state for new round (but keep folded status)"""
        self.current_bet = 0
        self.total_bet_this_round = 0
    
    def reset_for_new_hand(self) -> None:
        """Reset player state for a new hand"""
        self.reset_betting_state()
        self.folded = False
        self.all_in = False
        self.cards = []
        self.hand = None
    
    def ensure_cards_face_up(self) -> None:
        """Ensure all cards are face up"""
        for card in self.cards:
            if not card.faceup:
                card.faceup = True
    
    def __str__(self) -> str:
        """String representation of player"""
        status = []
        if self.folded:
            status.append("FOLDED")
        if self.all_in:
            status.append("ALL-IN")
        status_str = f" [{', '.join(status)}]" if status else ""
        return f"{self.name}: {self.chips} chips{status_str}"


class BettingRound:
    """Manages a single betting round"""
    
    MAX_ITERATIONS_MULTIPLIER = 10
    
    def __init__(self, game: 'PokerGame', round_name: str):
        self.game = game
        self.round_name = round_name
        self.current_bet = 0
        self.round_start_index = 0
        self.last_raiser = -1
    
    def execute(self) -> bool:
        """Execute betting round. Returns True if more than one player remains."""
        print(f"\n{'='*70}")
        print(f"{self.round_name} BETTING ROUND")
        print(f"{'='*70}\n")
        
        self._reset_betting_states()
        active_players = self._get_active_players()
        
        if len(active_players) <= 1:
            return False
        
        if self.round_name == "PRE-DRAW":
            self._post_blinds(active_players)
        
        return self._run_betting_loop()
    
    def _reset_betting_states(self) -> None:
        """Reset betting states for all players"""
        for player in self.game.players:
            player.reset_betting_state()
        self.current_bet = 0
    
    def _get_active_players(self) -> List[Player]:
        """Get list of active (non-folded) players"""
        return [p for p in self.game.players if p.is_active]
    
    def _post_blinds(self, active_players: List[Player]) -> None:
        """Post small and big blinds"""
        if len(active_players) < 2:
            return
        
        sb_player = active_players[0]
        bb_player = active_players[1]
        
        sb_bet = min(self.game.small_blind, sb_player.chips)
        bb_bet = min(self.game.big_blind, bb_player.chips)
        
        if sb_bet > 0:
            actual = sb_player.bet(sb_bet)
            self.game.pot += actual
            print(f"{sb_player.name} posts small blind: {sb_bet}")
        
        if bb_bet > 0:
            actual = bb_player.bet(bb_bet)
            self.game.pot += bb_bet
            print(f"{bb_player.name} posts big blind: {bb_bet}")
        
        self.current_bet = max(sb_player.current_bet, bb_player.current_bet)
    
    def _run_betting_loop(self) -> bool:
        """Run the main betting loop"""
        current_player_index = 0
        max_iterations = len(self.game.players) * self.MAX_ITERATIONS_MULTIPLIER
        
        for iteration in range(1, max_iterations + 1):
            active_players = [p for p in self.game.players if p.can_bet]
            
            if len(active_players) <= 1:
                break
            
            if self._is_betting_complete(current_player_index, iteration):
                break
            
            player = self.game.players[current_player_index]
            
            if not player.can_bet:
                current_player_index = (current_player_index + 1) % len(self.game.players)
                continue
            
            action = self._get_and_process_action(player)
            self._process_action(action, player, current_player_index)
            
            current_player_index = (current_player_index + 1) % len(self.game.players)
        
        return len(self._get_active_players()) > 1
    
    def _is_betting_complete(self, current_index: int, iteration: int) -> bool:
        """Check if betting round is complete"""
        all_matched = all(
            p.current_bet == self.current_bet or p.all_in
            for p in self.game.players if p.is_active
        )
        
        return all_matched and current_index == self.round_start_index and iteration > 1
    
    def _get_and_process_action(self, player: Player) -> str:
        """Get action from player and display game state"""
        print(f"\n{player.name}'s turn")
        self.game.display_hands(show_all=False, current_player=player)
        self.game.display_player_status()
        
        if isinstance(player.strategy, HumanPlayerStrategy):
            self._display_human_player_info(player)
        
        return player.strategy.get_betting_action(player, self.current_bet)
    
    def _display_human_player_info(self, player: Player) -> None:
        """Display information for human player"""
        print(f"Your hand: {' '.join(str(c) for c in player.cards)}")
        if player.hand:
            print(f"Hand rank: {player.hand.hand_name}")
        print(f"Your chips: {player.chips}")
        print(f"Current bet to match: {self.current_bet}")
        print(f"You have bet: {player.current_bet}")
    
    def _process_action(self, action: str, player: Player, player_index: int) -> None:
        """Process player's betting action"""
        if action == "fold":
            player.fold()
            print(f"{player.name} folds")
        elif action == "call":
            call_amount = self.current_bet - player.current_bet
            if call_amount > 0:
                actual_bet = player.bet(call_amount)
                self.game.pot += actual_bet
                print(f"{player.name} calls {actual_bet} chips")
            else:
                print(f"{player.name} checks")
        elif action.startswith("raise"):
            raise_amount = int(action.split()[1])
            total_needed = self.current_bet - player.current_bet + raise_amount
            actual_bet = player.bet(total_needed)
            self.game.pot += actual_bet
            self.current_bet = player.current_bet
            self.last_raiser = player_index
            self.round_start_index = (player_index + 1) % len(self.game.players)
            print(f"{player.name} raises by {raise_amount} chips (total bet: {player.current_bet})")


class DiscardPhase:
    """Manages the discard and draw phase"""
    
    MAX_DISCARD_COUNT = 3
    CARDS_IN_HAND = 5
    
    def __init__(self, game: 'PokerGame'):
        self.game = game
    
    def execute(self) -> None:
        """Execute discard and draw phase"""
        print("\n" + "="*70)
        print("DISCARD AND DRAW PHASE")
        print("="*70 + "\n")
        
        all_discards = self._collect_discards()
        self._return_discards_to_deck(all_discards)
        self._draw_replacement_cards()
    
    def _collect_discards(self) -> List[PlayingCard]:
        """Collect all discarded cards from players"""
        all_discards = []
        
        for player in self.game.players:
            if not player.is_active:
                continue
            
            self.game.display_hands(show_all=False, current_player=player)
            print(f"\n{player.name}'s turn")
            
            if isinstance(player.strategy, HumanPlayerStrategy):
                print(f"Your hand: {' '.join(str(c) for c in player.cards)}")
            
            discard_indices = player.strategy.get_discard_decision(player)
            
            # Discard cards
            for idx in discard_indices:
                if 0 <= idx < len(player.cards):
                    discarded = player.cards.pop(idx)
                    all_discards.append(discarded)
            
            self._display_discard_result(player, len(discard_indices))
        
        return all_discards
    
    def _display_discard_result(self, player: Player, discard_count: int) -> None:
        """Display result of discard decision"""
        if discard_count > 0:
            print(f"{player.name} discards {discard_count} card(s)")
        else:
            print(f"{player.name} keeps all cards")
    
    def _return_discards_to_deck(self, discards: List[PlayingCard]) -> None:
        """Return discarded cards to deck and shuffle"""
        for card in discards:
            self.game.deck.add(card)
        self.game.deck.shuffle()
    
    def _draw_replacement_cards(self) -> None:
        """Draw replacement cards for all players"""
        for player in self.game.players:
            if not player.is_active:
                continue
            
            cards_to_draw = self.CARDS_IN_HAND - len(player.cards)
            
            for _ in range(cards_to_draw):
                new_card = self.game.deck.deal()
                new_card.faceup = True
                player.cards.append(new_card)
            
            # Re-evaluate hand
            if len(player.cards) == self.CARDS_IN_HAND:
                player.hand = PokerHand(player.name, player.cards)
            
            if isinstance(player.strategy, HumanPlayerStrategy) and cards_to_draw > 0:
                print(f"Drew {cards_to_draw} new card(s)")
                print(f"Your new hand: {' '.join(str(c) for c in player.cards)}")


class Showdown:
    """Manages the showdown and winner determination"""
    
    def __init__(self, game: 'PokerGame'):
        self.game = game
    
    def execute(self) -> None:
        """Execute showdown and distribute pot"""
        print("\n" + "="*70)
        print("SHOWDOWN - RESULTS:")
        print("="*70)
        
        self._display_all_hands()
        active_players = self._get_active_players_with_hands()
        
        if not active_players:
            print("\nNo active players!")
            return
        
        if len(active_players) == 1:
            self._award_single_winner(active_players[0])
            return
        
        winners = self._determine_winners(active_players)
        self._display_ranked_hands(active_players)
        self._distribute_pot(winners)
    
    def _display_all_hands(self) -> None:
        """Display all players' hands"""
        print("\nAll players' hands:")
        for player in self.game.players:
            if not player.is_active:
                print(f"{player.name}: FOLDED")
            elif player.hand:
                cards_str = " ".join(str(c) for c in player.cards)
                print(f"{player.name}: {cards_str} - {player.hand.hand_name}")
            else:
                cards_str = " ".join(str(c) for c in player.cards)
                print(f"{player.name}: {cards_str}")
    
    def _get_active_players_with_hands(self) -> List[Player]:
        """Get active players who have hands"""
        return [p for p in self.game.players if p.is_active and p.hand]
    
    def _award_single_winner(self, winner: Player) -> None:
        """Award pot to single remaining player"""
        winner.chips += self.game.pot
        print(f"\n{winner.name} wins {self.game.pot} chips (all others folded)")
        self.game.pot = 0
    
    def _determine_winners(self, active_players: List[Player]) -> List[Player]:
        """Determine winning players"""
        sorted_hands = sorted([(p.hand, p) for p in active_players], key=lambda x: x[0], reverse=True)
        winner_hand = sorted_hands[0][0]
        
        return [
            p for p in active_players
            if p.hand.rank == winner_hand.rank
            and p.hand.tiebreakers == winner_hand.tiebreakers
        ]
    
    def _display_ranked_hands(self, active_players: List[Player]) -> None:
        """Display hands ranked from best to worst"""
        sorted_hands = sorted([(p.hand, p) for p in active_players], key=lambda x: x[0], reverse=True)
        
        print("\nHands ranked from best to worst:")
        for i, (hand, player) in enumerate(sorted_hands, 1):
            cards_str = " ".join(str(c) for c in player.cards)
            print(f"{i}. {player.name}: {cards_str} - {hand.hand_name}")
    
    def _distribute_pot(self, winners: List[Player]) -> None:
        """Distribute pot among winners"""
        pot_per_winner = self.game.pot // len(winners)
        remainder = self.game.pot % len(winners)
        
        print("\n" + "="*70)
        if len(winners) > 1:
            print("TIE! Winners:")
            for winner in winners:
                winner.chips += pot_per_winner
                if remainder > 0:
                    winner.chips += 1
                    remainder -= 1
                print(f"  {winner.name} - {winner.hand.hand_name} - wins {pot_per_winner} chips")
        else:
            winners[0].chips += self.game.pot
            print(f"WINNER: {winners[0].name}")
            print(f"Hand: {winners[0].hand.hand_name}")
            print(f"Wins: {self.game.pot} chips")
        
        self.game.pot = 0
        print("="*70 + "\n")


class PokerGame:
    """Poker game manager with betting"""
    
    MIN_PLAYERS = 1
    MAX_PLAYERS = 4
    DEFAULT_STARTING_CHIPS = 1000
    SMALL_BLIND = 10
    BIG_BLIND = 20
    
    def __init__(self, num_players: int, starting_chips: int = DEFAULT_STARTING_CHIPS):
        if not (self.MIN_PLAYERS <= num_players <= self.MAX_PLAYERS):
            raise ValueError(f"Number of players must be between {self.MIN_PLAYERS} and {self.MAX_PLAYERS}")
        
        self.num_players = num_players
        self.starting_chips = starting_chips
        self.deck = CardDeck()
        self.deck.shuffle()
        self.players: List[Player] = []
        self.pot = 0
        self.current_bet = 0
        self.dealer_position = 0
        self.small_blind = self.SMALL_BLIND
        self.big_blind = self.BIG_BLIND
        
        self._initialize_players()
    
    def _initialize_players(self) -> None:
        """Initialize players with appropriate strategies"""
        for i in range(self.num_players):
            name = f"Player {i+1}"
            strategy = HumanPlayerStrategy() if i == 0 else AIPlayerStrategy()
            self.players.append(Player(name, self.starting_chips, strategy))
    
    def deal_hands(self) -> None:
        """Deal 5 cards to each player"""
        self.deck = CardDeck()
        self.deck.shuffle()
        
        for player in self.players:
            player.cards = []
            player.hand = None
        
        # Deal cards in round-robin fashion
        for _ in range(PokerHand.CARDS_IN_HAND):
            for player in self.players:
                if player.is_active:
                    card = self.deck.deal()
                    card.faceup = True
                    player.cards.append(card)
        
        # Create PokerHand objects for active players
        for player in self.players:
            if player.is_active and len(player.cards) == PokerHand.CARDS_IN_HAND:
                player.hand = PokerHand(player.name, player.cards)
    
    def display_hands(self, show_all: bool = False, current_player: Optional[Player] = None) -> None:
        """Display all hands. If current_player is specified, show their cards face up."""
        print("\n" + "="*70)
        for player in self.players:
            if not player.is_active:
                print(f"{player.name}: FOLDED")
            elif show_all or player == current_player:
                player.ensure_cards_face_up()
                if player.hand:
                    cards_str = " ".join(str(c) for c in player.cards)
                    print(f"{player.name}: {cards_str} - {player.hand.hand_name}")
                else:
                    cards_str = " ".join(str(c) for c in player.cards)
                    print(f"{player.name}: {cards_str}")
            else:
                print(f"{player.name}: {' '.join('XX' for _ in player.cards)}")
        print("="*70 + "\n")
    
    def display_player_status(self) -> None:
        """Display player chips and betting status"""
        print("\n" + "="*70)
        print("PLAYER STATUS:")
        for player in self.players:
            bet_info = f" (bet: {player.current_bet})" if player.current_bet > 0 else ""
            print(f"{player}{bet_info}")
        print(f"Pot: {self.pot} chips")
        print(f"Current bet to match: {self.current_bet} chips")
        print("="*70 + "\n")
    
    def betting_round(self, round_name: str) -> bool:
        """Execute a betting round. Returns True if more than one player remains."""
        betting_round = BettingRound(self, round_name)
        return betting_round.execute()
    
    def discard_and_draw(self) -> None:
        """Allow players to discard and draw new cards"""
        discard_phase = DiscardPhase(self)
        discard_phase.execute()
    
    def determine_winner(self) -> None:
        """Determine and display the winner, distribute pot"""
        showdown = Showdown(self)
        showdown.execute()
    
    def play(self) -> None:
        """Main game loop with betting"""
        print("\n" + "="*70)
        print("WELCOME TO 5-CARD DRAW POKER WITH BETTING!")
        print("="*70)
        
        self._reset_for_new_hand()
        self.deal_hands()
        
        if not self.betting_round("PRE-DRAW"):
            self._handle_early_winner()
            return
        
        self.display_hands(show_all=False)
        self.discard_and_draw()
        
        if not self.betting_round("POST-DRAW"):
            self._handle_early_winner()
            return
        
        self.display_hands(show_all=True)
        self.determine_winner()
        self._display_final_chip_counts()
    
    def _reset_for_new_hand(self) -> None:
        """Reset game state for new hand"""
        self.pot = 0
        for player in self.players:
            player.reset_for_new_hand()
            if player.chips <= 0:
                player.chips = self.starting_chips  # Rebuy
    
    def _handle_early_winner(self) -> None:
        """Handle case where only one player remains"""
        active = [p for p in self.players if p.is_active]
        if active:
            winner = active[0]
            winner.chips += self.pot
            print(f"{winner.name} wins {self.pot} chips (all others folded)")
        else:
            print("All players folded - no winner")
        self.pot = 0
    
    def _display_final_chip_counts(self) -> None:
        """Display final chip counts for all players"""
        print("\n" + "="*70)
        print("FINAL CHIP COUNTS:")
        for player in self.players:
            print(f"{player.name}: {player.chips} chips")
        print("="*70 + "\n")


def get_user_input(prompt: str, validator, error_msg: str, default: Optional[int] = None) -> Optional[int]:
    """Get and validate user input. Returns default if input is empty."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                if default is not None:
                    return default
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
    print("5-CARD DRAW POKER GAME WITH BETTING")
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
        default=PokerGame.DEFAULT_STARTING_CHIPS
    ) or PokerGame.DEFAULT_STARTING_CHIPS
    
    game = PokerGame(num_players, starting_chips)
    
    while True:
        game.play()
        
        active_count = sum(1 for p in game.players if p.chips > 0)
        if active_count < 2:
            print("Game over! Not enough players with chips.")
            break
        
        while True:
            play_again = input("Play another hand? (y/n): ").strip().lower()
            if play_again in ('y', 'yes'):
                break
            elif play_again in ('n', 'no'):
                print("Thanks for playing!")
                return
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
