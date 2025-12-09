"""Pytest tests for cardlib_dataclass module"""
import pytest
from cardlib_dataclass import CardSuit, CardRank, PlayingCard, FaceCard, CardDeck


class TestCardSuit:
    """Test cases for CardSuit enum"""
    
    def test_suit_values(self):
        """Test suit enum values"""
        assert CardSuit.CLUBS.value == 0
        assert CardSuit.DIAMONDS.value == 1
        assert CardSuit.HEARTS.value == 2
        assert CardSuit.SPADES.value == 3
    
    def test_suit_symbols(self):
        """Test suit symbols"""
        assert CardSuit.CLUBS.symbol == '\u2663'
        assert CardSuit.DIAMONDS.symbol == '\u2666'
        assert CardSuit.HEARTS.symbol == '\u2665'
        assert CardSuit.SPADES.symbol == '\u2660'


class TestCardRank:
    """Test cases for CardRank enum"""
    
    def test_rank_values(self):
        """Test rank enum values"""
        assert CardRank.ACE.value == 1
        assert CardRank.TWO.value == 2
        assert CardRank.KING.value == 13
    
    def test_rank_comparison(self):
        """Test rank comparison operators"""
        assert CardRank.ACE < CardRank.TWO
        assert CardRank.KING > CardRank.QUEEN


class TestPlayingCard:
    """Test cases for PlayingCard dataclass"""
    
    def test_card_creation(self):
        """Test creating a valid card"""
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        assert card.rank == CardRank.ACE
        assert card.suit == CardSuit.CLUBS
        assert card.faceup == False
    
    def test_card_creation_face_up(self):
        """Test creating a card face up"""
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS, faceup=True)
        assert card.faceup == True
    
    def test_card_str_face_down(self):
        """Test string representation of face down card"""
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        assert str(card) == "XX"
    
    def test_card_str_face_up(self):
        """Test string representation of face up card"""
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS, faceup=True)
        assert str(card) == "A\u2663"
    
    def test_card_properties(self):
        """Test card properties"""
        card = PlayingCard(rank=CardRank.KING, suit=CardSuit.SPADES)
        assert card.rank == CardRank.KING
        assert card.suit == CardSuit.SPADES
        assert card.value == 13
    
    def test_card_flip(self):
        """Test flipping a card"""
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        assert card.faceup == False
        card.flip()
        assert card.faceup == True
        card.flip()
        assert card.faceup == False
    
    def test_card_hash(self):
        """Test card hashing"""
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        assert isinstance(hash(card), int)
    
    def test_card_equality(self):
        """Test card equality (dataclass default)"""
        card1 = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        card2 = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        assert card1 == card2


class TestFaceCard:
    """Test cases for FaceCard dataclass"""
    
    def test_face_card_creation_valid(self):
        """Test creating a valid face card"""
        card = FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS)
        assert card.rank == CardRank.JACK
        assert card.suit == CardSuit.CLUBS
        assert card.eyes == 2
    
    def test_face_card_creation_invalid_rank(self):
        """Test creating a face card with invalid rank"""
        with pytest.raises(ValueError, match='invalid face card rank'):
            FaceCard(rank=CardRank.NINE, suit=CardSuit.CLUBS)
    
    def test_one_eyed_jack_hearts(self):
        """Test one-eyed Jack of Hearts"""
        card = FaceCard(rank=CardRank.JACK, suit=CardSuit.HEARTS)
        assert card.eyes == 1
    
    def test_one_eyed_jack_spades(self):
        """Test one-eyed Jack of Spades"""
        card = FaceCard(rank=CardRank.JACK, suit=CardSuit.SPADES)
        assert card.eyes == 1
    
    def test_one_eyed_king_diamonds(self):
        """Test one-eyed King of Diamonds"""
        card = FaceCard(rank=CardRank.KING, suit=CardSuit.DIAMONDS)
        assert card.eyes == 1
    
    def test_two_eyed_face_card(self):
        """Test two-eyed face card"""
        card = FaceCard(rank=CardRank.QUEEN, suit=CardSuit.CLUBS)
        assert card.eyes == 2
    
    def test_face_card_str_face_down(self):
        """Test string representation of face down face card"""
        card = FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS)
        assert str(card) == "XX"
    
    def test_face_card_str_face_up(self):
        """Test string representation of face up face card"""
        card = FaceCard(rank=CardRank.JACK, suit=CardSuit.CLUBS)
        card.faceup = True
        assert str(card) == "J\u26632"


class TestCardDeck:
    """Test cases for CardDeck class"""
    
    def test_deck_creation(self):
        """Test creating a deck"""
        deck = CardDeck()
        assert len(deck) == 52
    
    def test_deck_deal(self):
        """Test dealing a card from the deck"""
        deck = CardDeck()
        initial_size = len(deck)
        card = deck.deal()
        assert len(deck) == initial_size - 1
        assert isinstance(card, (PlayingCard, FaceCard))
        assert card.faceup == False
    
    def test_deck_add(self):
        """Test adding a card back to the deck"""
        deck = CardDeck()
        card = PlayingCard(rank=CardRank.ACE, suit=CardSuit.CLUBS)
        card.faceup = False
        initial_size = len(deck)
        deck.add(card)
        assert len(deck) == initial_size + 1
        assert card.faceup == True
    
    def test_deck_shuffle(self):
        """Test shuffling the deck"""
        deck = CardDeck()
        original_order = deck._cardstack.copy()
        deck.shuffle()
        assert len(deck._cardstack) == len(original_order)
        assert set(id(c) for c in deck._cardstack) == set(id(c) for c in original_order)
    
    def test_deck_deal_all_cards(self):
        """Test dealing all cards from the deck"""
        deck = CardDeck()
        cards = []
        for _ in range(52):
            cards.append(deck.deal())
        assert len(deck) == 0
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
