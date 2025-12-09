"This libary is an implementation of a CardDeck and associated classes using Enums"
from enum import Enum
import random

class CardSuit(Enum):
    """This class represents Card Suits"""
    def __init__(self, value:int, symbol:str, displayname:str):
        self._value_ = value
        self.symbol = symbol
        self.displayname = displayname
    
    CLUBS = (0, '\u2663', 'Clubs')
    DIAMONDS = (1, '\u2666', 'Diamonds')
    HEARTS = (2, '\u2665', 'Hearts')
    SPADES = (3, '\u2660', 'Spades')

class CardRank(Enum):
    """This class represents Card Ranks"""
    def __init__(self, value:int, symbol:str, displayname:str):
        self._value_ = value
        self.symbol = symbol
        self.displayname = displayname


    def __lt__(self,other):
        return self.value < other.value

    def __le__(self,other):
        return self.value <= other.value

    def __gt__(self,other):
        return self.value > other.value

    def __ge__(self,other):
        return self.value >= other.value

    ACE = (1, "A", "Ace")
    TWO = (2, "2", "Two")
    THREE = (3, "3", "Three")
    FOUR = (4, "4", "Four")
    FIVE = (5, "5", "Five")
    SIX = (6, "6", "Six")
    SEVEN = (7, "7", "Seven")
    EIGHT = (8, "8", "Eight")
    NINE = (9, "9", "Nine")
    TEN = (10, "T", "Ten")
    JACK = (11, "J", "Jack")
    QUEEN = (12, "Q", "Queen")
    KING = (13, "K", "King")

class PlayingCard():
    """ This class represents a Playing Card"""

    def __init__(self, rank:CardRank, suit:CardSuit):
        self._rank = rank
        self._suit = suit
        self._faceup = False

    def __str__(self) -> str:
        if not self.faceup:
            return "XX"
        else:
            # return f"{self._rank} of {self._suit}"
            # return f"{self.rank_name} of {self.suit_name}"
            return f"{self._rank.symbol}{self._suit.symbol}"

    def __repr__(self) -> str:
        return f"PlayingCard(rank={self._rank}, suit={self._suit})"

    def __eq__(self, other: 'PlayingCard') -> bool:
        return self._rank == other._rank and self._suit == other._suit

    def __hash__(self):
        return hash((self._rank, self._suit))

    @property
    def value(self) -> int:
        """This property returns the value of a card"""
        return self._rank.value

    @property
    def rank(self) -> CardRank:
        """This property returns the card's rank"""
        return self._rank

    @property
    def suit(self) -> CardSuit:
        """This property returns the card's suit"""
        return self._suit

    @property
    def faceup(self) -> bool:
        """This property returns if the card is face up or not"""
        return self._faceup

    @faceup.setter
    def faceup(self, value: bool) -> None:
        self._faceup = value

    def flip(self) -> None:
        """This method flips a card"""
        self._faceup = not self._faceup

class FaceCard(PlayingCard):
    """This class represents a Face Card"""

    ONE_EYED = frozenset({(CardRank.JACK, CardSuit.HEARTS), 
                          (CardRank.JACK, CardSuit.SPADES), 
                          (CardRank.KING, CardSuit.DIAMONDS)})

    def __init__(self, rank:CardRank, suit:CardSuit):
        if rank < CardRank.JACK:
            raise ValueError('invalid face card rank')
        super().__init__(rank, suit)
        # self._eyes = 2
        # if rank == CardRank.JACK and suit == CardSuit.HEARTS:
        #     self._eyes = 1
        # if rank == CardRank.JACK and suit == CardSuit.SPADES:
        #     self._eyes = 1
        # if rank == CardRank.KING and suit == CardSuit.DIAMONDS:
        #     self._eyes = 1
        self._eyes = 1 if (rank, suit) in FaceCard.ONE_EYED else 2
    # def __init__(self,eyes:int, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._eyes = eyes

    @property
    def eyes(self) -> int:
        """This method returns the number of eyes on a FaceCard"""
        return self._eyes

    def __str__(self) -> str:
        base = super().__str__()
        return base if not self.faceup else f"{base}{self._eyes}"

    def __repr__(self) -> str:
        return f"FaceCard(rank={self.rank}, suit={self.suit})"

class CardDeck():
    """ This class represents a Card Deck"""
    def __init__(self):
        self._cardstack = []
        for s in CardSuit:
            for r in CardRank:
                if r < CardRank.JACK:
                    c = PlayingCard(r,s)
                else:
                    c = FaceCard(r,s)
                c.flip()
                self._cardstack.append(c)

    def __len__(self) -> int:
        return len(self._cardstack)

    # def __str__(self) -> str:
    #     ret = ""
    #     for card in self._cardstack:
    #         ret += str(card) + " "
    #     return ret
    def __str__(self) -> str:
        return " ".join(str(card) for card in self._cardstack)

    def deal(self) -> PlayingCard:
        """This method deals a card from the deck"""
        c = self._cardstack.pop()
        c.flip()
        return c

    def add(self, c:PlayingCard) -> None:
        """This method adds a card back to the deck"""
        c.faceup = True
        self._cardstack.append(c)

    def shuffle(self) -> None:
        """This method shuffles the deck"""
        # nc = len(self._cardstack)-1
        # for ix in range(nc):
        #     ixswap = randint(0, nc)
        #     temp = self._cardstack[ixswap]
        #     self._cardstack[ixswap] = self._cardstack[ix]
        #     self._cardstack[ix] = temp
        random.shuffle(self._cardstack)


if __name__ == "__main__":
    d = CardDeck()

    print(str(d))
    d.shuffle()
    print(str(d))

    print(f'value={CardSuit.CLUBS.value}, name={CardSuit.CLUBS.name}, ' \
          f'symbol={CardSuit.CLUBS.symbol}, displayname={CardSuit.CLUBS.displayname}')
