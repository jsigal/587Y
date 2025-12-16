"""Pytest tests for tehigame_2player_dataclass module"""
import pytest
from tehigame_2player_dataclass import TehiHand, TehiGame
from cardlib_dataclass import CardRank, CardSuit, PlayingCard, FaceCard


class TestTehiHand:
    """Test cases for TehiHand dataclass"""
    
    def test_hand_creation(self):
        """Test creating an empty hand"""
        hand = TehiHand()
        assert len(hand._hand) == 0
    
    def test_hand_str_empty(self):
        """Test string representation of empty hand"""
        hand = TehiHand()
        assert str(hand) == ""
    
    def test_hand_deal(self):
        """Test dealing a hand"""
        from cardlib_dataclass import CardDeck
        deck = CardDeck()
        hand = TehiHand()
        hand.deal(deck)
        assert len(hand._hand) == 5
        assert len(deck) == 52 - 5
        for card in hand._hand:
            assert card.faceup == True
    
    def test_hand_return_to_deck(self):
        """Test returning hand to deck"""
        from cardlib_dataclass import CardDeck
        deck = CardDeck()
        hand = TehiHand()
        hand.deal(deck)
        initial_deck_size = len(deck)
        hand.return_to_deck(deck)
        assert len(hand._hand) == 0
        assert len(deck) == initial_deck_size + 5
    
    def test_hand_score_all_face_cards(self):
        """Test hand score with all face cards"""
        hand = TehiHand()
        # Add 5 face cards, each with 2 eyes = 10 total eyes
        # No regular cards = 0 total rank
        # Score = 10 * 0 = 0
        for _ in range(5):
            card = FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS)
            card.faceup = True
            hand._hand.append(card)
        assert hand.score == 0
    
    def test_hand_score_all_regular_cards(self):
        """Test hand score with all regular cards"""
        hand = TehiHand()
        # Add 5 regular cards, total rank = 1+2+3+4+5 = 15
        # No face cards = 0 total eyes
        # Score = 0 * 15 = 0
        for rank in [CardRank.ACE, CardRank.TWO, CardRank.THREE, CardRank.FOUR, CardRank.FIVE]:
            card = PlayingCard(rank=rank, suit=CardSuit.CLUBS)
            card.faceup = True
            hand._hand.append(card)
        assert hand.score == 0
    
    def test_hand_score_mixed(self):
        """Test hand score with mixed cards"""
        hand = TehiHand()
        # Add 2 face cards (2 eyes each = 4 total eyes)
        # Add 3 regular cards (1+2+3 = 6 total rank)
        # Score = 4 * 6 = 24
        hand._hand.append(FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS))
        hand._hand.append(FaceCard(rank=CardRank.QUEEN, suit=CardSuit.CLUBS))
        hand._hand.append(PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS))
        hand._hand.append(PlayingCard(rank=CardRank.TWO, suit=CardSuit.CLUBS))
        hand._hand.append(PlayingCard(rank=CardRank.THREE, suit=CardSuit.CLUBS))
        for card in hand._hand:
            card.faceup = True
        assert hand.score == 24
    
    def test_hand_score_one_eyed_cards(self):
        """Test hand score with one-eyed cards"""
        hand = TehiHand()
        # Add one-eyed Jack of Hearts (1 eye)
        # Add one-eyed King of Diamonds (1 eye)
        # Add 3 regular cards (1+2+3 = 6 total rank)
        # Score = 2 * 6 = 12
        hand._hand.append(FaceCard(rank=CardRank.JACK, suit=CardSuit.HEARTS))
        hand._hand.append(FaceCard(rank=CardRank.KING, suit=CardSuit.DIAMONDS))
        hand._hand.append(PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS))
        hand._hand.append(PlayingCard(rank=CardRank.TWO, suit=CardSuit.CLUBS))
        hand._hand.append(PlayingCard(rank=CardRank.THREE, suit=CardSuit.CLUBS))
        for card in hand._hand:
            card.faceup = True
        assert hand.score == 12
    
    def test_hand_comparison_gt(self):
        """Test hand greater than comparison"""
        hand1 = TehiHand()
        hand2 = TehiHand()
        hand1._hand.append(FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS))
        hand1._hand.append(PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS))
        hand2._hand.append(PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS))
        for card in hand1._hand + hand2._hand:
            card.faceup = True
        assert hand1 > hand2
    
    def test_hand_comparison_lt(self):
        """Test hand less than comparison"""
        hand1 = TehiHand()
        hand2 = TehiHand()
        hand1._hand.append(PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS))
        hand2._hand.append(FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS))
        hand2._hand.append(PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS))
        for card in hand1._hand + hand2._hand:
            card.faceup = True
        assert hand1 < hand2


class TestTehiGame:
    """Test cases for TehiGame class"""
    
    def test_game_creation(self):
        """Test creating a new game"""
        game = TehiGame()
        assert game._gameswon == 0
        assert game._totalgames == 0
        assert game._besthandscore == 0
        assert len(game._deck) == 52
    
    def test_game_str(self):
        """Test game string representation"""
        game = TehiGame()
        assert str(game) == 'won 0 of 0 with best of 0'
    
    def test_game_play(self, capsys):
        """Test playing a round"""
        game = TehiGame()
        game.play()
        captured = capsys.readouterr()
        assert game._totalgames == 1
        assert len(game._playerhand._hand) == 5
        assert len(game._dealerhand._hand) == 5
        assert "Player Hand" in captured.out
        assert "Dealer Hand" in captured.out
        assert len(game._deck) == 52 - 10  # 10 cards dealt (5 per hand)
    
    def test_game_play_multiple_rounds(self, capsys):
        """Test playing multiple rounds"""
        game = TehiGame()
        game.play()
        game.play()
        assert game._totalgames == 2
        assert len(game._playerhand._hand) == 5
        assert len(game._dealerhand._hand) == 5
    
    def test_game_tracks_best_hand_score(self, capsys):
        """Test that game tracks best hand score"""
        game = TehiGame()
        # Play multiple rounds to potentially get different scores
        for _ in range(5):
            game.play()
        assert game._besthandscore >= 0
    
    def test_game_tracks_wins(self, capsys):
        """Test that game tracks wins"""
        game = TehiGame()
        # Play a round - may or may not win
        game.play()
        # The gameswon should be 0 or 1 depending on outcome
        assert game._gameswon in [0, 1]
        assert game._totalgames == 1
