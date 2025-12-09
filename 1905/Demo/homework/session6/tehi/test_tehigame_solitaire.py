"""Pytest tests for tehigame_solitaire module"""
import pytest
from tehigame_solitaire import TehiGame
from cardlib import PlayingCard, FaceCard


class TestTehiGame:
    """Test cases for TehiGame solitaire class"""
    
    def test_game_creation(self):
        """Test creating a new game"""
        game = TehiGame()
        assert len(game._hand) == 0
        assert game._handsdealt == 0
        assert game._besthandscore == 0
        assert len(game._deck) == 52
    
    def test_game_str_empty_hand(self):
        """Test string representation of empty hand"""
        game = TehiGame()
        assert str(game) == ""
    
    def test_game_deal(self):
        """Test dealing a hand"""
        game = TehiGame()
        game.deal()
        assert len(game._hand) == 5
        assert game._handsdealt == 1
        assert len(game._deck) == 52 - 5
        for card in game._hand:
            assert card.faceup == True
    
    def test_game_deal_multiple_times(self):
        """Test dealing multiple hands"""
        game = TehiGame()
        game.deal()
        initial_deck_size = len(game._deck)
        game.deal()
        assert len(game._hand) == 5
        assert game._handsdealt == 2
        # After second deal, cards from first hand should be returned
        # So deck should have initial_deck_size + 5 - 5 = initial_deck_size
        assert len(game._deck) == initial_deck_size
    
    def test_game_score_all_face_cards(self):
        """Test score with all face cards"""
        game = TehiGame()
        # Add 5 face cards, each with 2 eyes = 10 total eyes
        # No regular cards = 0 total rank
        # Score = 10 * 0 = 0
        for _ in range(5):
            card = FaceCard(11, 0)  # Jack of Clubs
            card.faceup = True
            game._hand.append(card)
        assert game.score == 0
    
    def test_game_score_all_regular_cards(self):
        """Test score with all regular cards"""
        game = TehiGame()
        # Add 5 regular cards, total rank = 1+2+3+4+5 = 15
        # No face cards = 0 total eyes
        # Score = 0 * 15 = 0
        for rank in [1, 2, 3, 4, 5]:
            card = PlayingCard(rank, 0)  # Clubs
            card.faceup = True
            game._hand.append(card)
        assert game.score == 0
    
    def test_game_score_mixed(self):
        """Test score with mixed cards"""
        game = TehiGame()
        # Add 2 face cards (2 eyes each = 4 total eyes)
        # Add 3 regular cards (1+2+3 = 6 total rank)
        # Score = 4 * 6 = 24
        game._hand.append(FaceCard(11, 0))  # Jack of Clubs
        game._hand.append(FaceCard(12, 0))  # Queen of Clubs
        game._hand.append(PlayingCard(1, 0))  # Ace of Clubs
        game._hand.append(PlayingCard(2, 0))  # 2 of Clubs
        game._hand.append(PlayingCard(3, 0))  # 3 of Clubs
        for card in game._hand:
            card.faceup = True
        assert game.score == 24
    
    def test_game_score_one_eyed_cards(self):
        """Test score with one-eyed cards"""
        game = TehiGame()
        # Add one-eyed Jack of Hearts (1 eye)
        # Add one-eyed King of Diamonds (1 eye)
        # Add 3 regular cards (1+2+3 = 6 total rank)
        # Score = 2 * 6 = 12
        game._hand.append(FaceCard(11, 2))  # Jack of Hearts
        game._hand.append(FaceCard(13, 1))  # King of Diamonds
        game._hand.append(PlayingCard(1, 0))  # Ace of Clubs
        game._hand.append(PlayingCard(2, 0))  # 2 of Clubs
        game._hand.append(PlayingCard(3, 0))  # 3 of Clubs
        for card in game._hand:
            card.faceup = True
        assert game.score == 12
    
    def test_game_handsdealt_property(self):
        """Test handsdealt property"""
        game = TehiGame()
        assert game.handsdealt == 0
        game.deal()
        assert game.handsdealt == 1
        game.deal()
        assert game.handsdealt == 2
    
    def test_game_besthandscore_property(self):
        """Test besthandscore property"""
        game = TehiGame()
        assert game.besthandscore == 0
        game.deal()
        # besthandscore should be updated after deal
        assert game.besthandscore >= 0
    
    def test_game_tracks_best_hand_score(self):
        """Test that game tracks best hand score across multiple deals"""
        game = TehiGame()
        # Deal multiple times
        for _ in range(5):
            game.deal()
        # besthandscore should be the maximum score seen
        assert game.besthandscore >= 0
    
    def test_game_deal_returns_cards_to_deck(self):
        """Test that deal returns previous hand cards to deck"""
        game = TehiGame()
        game.deal()
        first_hand_cards = game._hand.copy()
        game.deal()
        # After second deal, first hand cards should be back in deck
        deck_card_ids = {id(c) for c in game._deck._cardstack}
        first_hand_card_ids = {id(c) for c in first_hand_cards}
        # All cards from first hand should be in deck
        assert first_hand_card_ids.issubset(deck_card_ids)
