"""Pytest tests for cardlib module"""
import pytest
from cardlib import PlayingCard, FaceCard, CardDeck


class TestPlayingCard:
    """Test cases for PlayingCard class"""
    
    def test_card_creation_valid(self):
        """Test creating a valid card"""
        card = PlayingCard(1, 0)  # Ace of Clubs
        assert card.rank == 1
        assert card.suit == 0
        assert card.faceup == False
    
    def test_card_creation_invalid_rank(self):
        """Test creating a card with invalid rank"""
        with pytest.raises(ValueError, match='Invalid card rank'):
            PlayingCard(14, 0)
    
    def test_card_creation_invalid_suit(self):
        """Test creating a card with invalid suit"""
        with pytest.raises(ValueError, match='Invalid card suit'):
            PlayingCard(1, 4)
    
    def test_card_str_face_down(self):
        """Test string representation of face down card"""
        card = PlayingCard(1, 0)
        assert str(card) == "XX"
    
    def test_card_str_face_up(self):
        """Test string representation of face up card"""
        card = PlayingCard(1, 0)  # Ace of Clubs
        card.faceup = True
        assert str(card) == "A\u2663"
    
    def test_card_properties(self):
        """Test card properties"""
        card = PlayingCard(13, 3)  # King of Spades
        assert card.rank == 13
        assert card.suit == 3
        assert card.value == 13
        assert card.rank_str == "K"
        assert card.suit_str == "\u2660"
        assert card.rank_name == "King"
        assert card.suit_name == "Spades"
        assert card.string == "K\u2660"
        assert card.name == "King of Spades"
    
    def test_card_flip(self):
        """Test flipping a card"""
        card = PlayingCard(1, 0)
        assert card.faceup == False
        card.flip()
        assert card.faceup == True
        card.flip()
        assert card.faceup == False
    
    def test_faceup_setter(self):
        """Test faceup setter"""
        card = PlayingCard(1, 0)
        card.faceup = True
        assert card.faceup == True
        card.faceup = False
        assert card.faceup == False


class TestFaceCard:
    """Test cases for FaceCard class"""
    
    def test_face_card_creation_valid(self):
        """Test creating a valid face card"""
        card = FaceCard(11, 0)  # Jack of Clubs
        assert card.rank == 11
        assert card.suit == 0
        assert card.eyes == 2
    
    def test_face_card_creation_invalid_rank(self):
        """Test creating a face card with invalid rank"""
        with pytest.raises(ValueError, match='invalid face card rank'):
            FaceCard(9, 0)
    
    def test_one_eyed_jack_hearts(self):
        """Test one-eyed Jack of Hearts"""
        card = FaceCard(11, 2)  # Jack of Hearts
        assert card.eyes == 1
    
    def test_one_eyed_jack_spades(self):
        """Test one-eyed Jack of Spades"""
        card = FaceCard(11, 3)  # Jack of Spades
        assert card.eyes == 1
    
    def test_one_eyed_king_diamonds(self):
        """Test one-eyed King of Diamonds"""
        card = FaceCard(13, 1)  # King of Diamonds
        assert card.eyes == 1
    
    def test_two_eyed_face_card(self):
        """Test two-eyed face card"""
        card = FaceCard(12, 0)  # Queen of Clubs
        assert card.eyes == 2
    
    def test_face_card_str_face_down(self):
        """Test string representation of face down face card"""
        card = FaceCard(11, 0)
        assert str(card) == "XX"
    
    def test_face_card_str_face_up(self):
        """Test string representation of face up face card"""
        card = FaceCard(11, 0)  # Jack of Clubs
        card.faceup = True
        assert str(card) == "J\u26632"


class TestCardDeck:
    """Test cases for CardDeck class"""
    
    def test_deck_creation(self):
        """Test creating a deck"""
        deck = CardDeck()
        assert len(deck._cardstack) == 52
    
    def test_deck_deal(self):
        """Test dealing a card from the deck"""
        deck = CardDeck()
        initial_size = len(deck._cardstack)
        card = deck.deal()
        assert len(deck._cardstack) == initial_size - 1
        assert isinstance(card, (PlayingCard, FaceCard))
        assert card.faceup == False
    
    def test_deck_add(self):
        """Test adding a card back to the deck"""
        deck = CardDeck()
        card = PlayingCard(1, 0)
        card.faceup = False
        initial_size = len(deck._cardstack)
        deck.add(card)
        assert len(deck._cardstack) == initial_size + 1
        assert card.faceup == True
    
    def test_deck_shuffle(self):
        """Test shuffling the deck"""
        deck = CardDeck()
        original_order = deck._cardstack.copy()
        deck.shuffle()
        # Very unlikely that shuffle produces same order
        # But we can check that all cards are still present
        assert len(deck._cardstack) == len(original_order)
        assert set(id(c) for c in deck._cardstack) == set(id(c) for c in original_order)
    
    def test_deck_deal_all_cards(self):
        """Test dealing all cards from the deck"""
        deck = CardDeck()
        cards = []
        for _ in range(52):
            cards.append(deck.deal())
        assert len(deck._cardstack) == 0
        assert len(cards) == 52
    
    def test_deck_contains_face_cards(self):
        """Test that deck contains face cards"""
        deck = CardDeck()
        face_cards = [c for c in deck._cardstack if isinstance(c, FaceCard)]
        assert len(face_cards) == 12  # 4 suits * 3 face cards (J, Q, K)
    
    def test_deck_contains_regular_cards(self):
        """Test that deck contains regular cards"""
        deck = CardDeck()
        regular_cards = [c for c in deck._cardstack if isinstance(c, PlayingCard) and not isinstance(c, FaceCard)]
        assert len(regular_cards) == 40  # 4 suits * 10 regular cards (A-10)
