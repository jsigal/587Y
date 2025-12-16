"This libary is an implementation of a CardDeck and associated classes using Enums and Dataclasses"
from enum import Enum
from dataclasses import dataclass, field
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

@dataclass
class PlayingCard:
    """This class represents a Playing Card"""
    rank: CardRank
    suit: CardSuit
    faceup: bool = field(default=False, compare=False)

    def __str__(self) -> str:
        if not self.faceup:
            return "XX"
        return f"{self.rank.symbol}{self.suit.symbol}"

    def __hash__(self):
        return hash((self.rank, self.suit))

    @property
    def value(self) -> int:
        """This property returns the value of a card"""
        return self.rank.value

    def flip(self) -> None:
        """This method flips a card"""
        self.faceup = not self.faceup

@dataclass
class FaceCard(PlayingCard):
    """This class represents a Face Card"""
    ONE_EYED = frozenset({(CardRank.JACK, CardSuit.HEARTS), 
                          (CardRank.JACK, CardSuit.SPADES), 
                          (CardRank.KING, CardSuit.DIAMONDS)})

    eyes: int = field(init=False)

    def __post_init__(self):
        if self.rank < CardRank.JACK:
            raise ValueError('invalid face card rank')
        self.eyes = 1 if (self.rank, self.suit) in FaceCard.ONE_EYED else 2

    def __str__(self) -> str:
        base = super().__str__()
        return base if not self.faceup else f"{base}{self.eyes}"

class CardDeck():
    """ This class represents a Card Deck"""
    def __init__(self):
        # self._cardstack = []
        # for s in CardSuit:
        #     for r in CardRank:
        #         if r < CardRank.JACK:
        #             c = PlayingCard(r,s)
        #         else:
        #             c = FaceCard(r,s)
        #         c.flip()
        #         self._cardstack.append(c)
        self._cardstack = [
            FaceCard(suit=suit, rank=rank) 
                if rank in [CardRank.JACK, CardRank.QUEEN, CardRank.KING]
                else PlayingCard(suit=suit, rank=rank)
            for suit in CardSuit
            for rank in CardRank ]
        for card in self._cardstack:
            card.flip()

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
