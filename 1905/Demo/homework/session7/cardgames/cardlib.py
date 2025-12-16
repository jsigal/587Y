"This libary is an implementation of a CardDeck and associated classes"
from typing import Tuple
from random import randint

class PlayingCard():
    """ This class represents a Playing Card"""
    ranks : Tuple[int] = (1,2,3,4,5,6,7,8,9,10,11,12,13)
    RANK_NAME : Tuple[str] = ("","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
    RANK_STR : Tuple[str] = ("","A","2","3","4","5","6","7","8","9","10","J","Q","K")
    suits : Tuple[int] = (0,1,2,3)
    SUIT_NAME : Tuple[str] = ("Clubs", "Diamonds", "Hearts", "Spades")
    SUIT_STR : Tuple[str] = ("\u2663","\u2666","\u2665","\u2660")
    SUIT_CLUB : int = 0
    SUIT_DIAMOND : int = 1
    SUIT_HEART : int = 2
    SUIT_SPADE : int = 3
    RANK_ACE : int = 0
    RANK_JACK : int = 11
    RANK_QUEEN : int = 12
    RANK_KING : int = 13

    def __init__(self, rank:int, suit:int):
        if rank not in PlayingCard.ranks:
            raise ValueError('Invalid card rank')
        if suit not in PlayingCard.suits:
            raise ValueError('Invalid card suit')
        self._rank = rank
        self._suit = suit
        self._faceup = False

    def __str__(self) -> str:
        if not self.faceup:
            return "XX"
        else:
            # return f"{self._rank} of {self._suit}"
            # return f"{self.rank_name} of {self.suit_name}"
            return f"{self.rank_str}{self.suit_str}"

    def __repr__(self) -> str:
        return f"PlayingCard('rank={self._rank}, suit={self._suit})"

    @property
    def rank(self) -> int:
        """This property returns the card's rank"""
        return self._rank

    @property
    def suit(self) -> int:
        """This property returns the card's suit"""
        return self._suit

    @property
    def faceup(self) -> bool:
        """This property returns if the card is face up or not"""
        return self._faceup

    @faceup.setter
    def faceup(self, value) -> None:
        self._faceup = value

    @property
    def value(self) -> int:
        """This property returns the value of a card"""
        return self._rank

    @property
    def rank_str(self) -> str:
        """This property returns the card's rank string"""
        return PlayingCard.RANK_STR[self._rank]

    @property
    def suit_str(self) -> str:
        """This property returns the card's suit string"""
        return PlayingCard.SUIT_STR[self._suit]

    @property
    def rank_name(self) -> str:
        """This property returns the card's rank name"""
        return PlayingCard.RANK_NAME[self._rank]

    @property
    def suit_name(self) -> str:
        """This property returns the card's suit name"""
        return PlayingCard.SUIT_NAME[self._suit]

    @property
    def string(self) -> str:
        """This property returns the card as a string"""
        return f'{self.rank_str}{self.suit_str}'

    @property
    def name(self) -> str:
        """This property returns the card as a name"""
        return f'{self.rank_name} of {self.suit_name}'

    def flip(self) -> None:
        """This method flips a card"""
        self._faceup = not self._faceup

class FaceCard(PlayingCard):
    """This class represents a Face Card"""
    def __init__(self, rank:int, suit:int):
        if rank < 10:
            raise ValueError('invalid face card rank')
        super().__init__(rank, suit)
        self._eyes = 2
        if rank == PlayingCard.RANK_JACK and suit == PlayingCard.SUIT_HEART:
            self._eyes = 1
        if rank == PlayingCard.RANK_JACK and suit == PlayingCard.SUIT_SPADE:
            self._eyes = 1
        if rank == PlayingCard.RANK_KING and suit == PlayingCard.SUIT_DIAMOND:
            self._eyes = 1
    # def __init__(self,eyes:int, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._eyes = eyes

    @property
    def eyes(self) -> int:
        """This method returns the number of eyes on a FaceCard"""
        return self._eyes

    def __str__(self) -> str:
        if not self.faceup:
            return super().__str__()
        else:
            # return super().__str__() + f" with {self._eyes} eyes"
            return super().__str__() + f"{self._eyes}"

    def __repr__(self) -> str:
        return f"FaceCard(rank={self.rank}, suit={self.suit})"

class CardDeck():
    """ This class represents a Card Deck"""
    def __init__(self):
        self._cardstack = []
        for s in PlayingCard.suits:
            for r in PlayingCard.ranks:
                if r < PlayingCard.RANK_JACK:
                    c = PlayingCard(r,s)
                else:
                    c = FaceCard(r,s)
                c.flip()
                self._cardstack.append(c)

    def __str__(self) -> str:
        ret = ""
        for card in self._cardstack:
            ret += str(card) + " "
        return ret
    def __len__(self) -> int:
        """This method returns the number of cards in the deck"""
        return len(self._cardstack)
        
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
        nc = len(self._cardstack)-1
        for ix in range(nc):
            ixswap = randint(0, nc)
            temp = self._cardstack[ixswap]
            self._cardstack[ixswap] = self._cardstack[ix]
            self._cardstack[ix] = temp

if __name__ == "__main__":
    d = CardDeck()

    print(str(d))
    d.shuffle()
    print(str(d))
