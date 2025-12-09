"""This is an implementation of 2 player The Eyes Have It"""
from dataclasses import dataclass, field
from cardlib_dataclass import FaceCard, CardDeck

@dataclass
class TehiHand:
    """This class represents a Tehi Hand"""
    _hand: list = field(default_factory=list)

    def __str__(self) -> str:
        return " ".join(str(card) for card in self._hand)

    @property
    def score(self) -> int:
        """This property calculates the score of a hand"""
        te = sum(c.eyes for c in self._hand if isinstance(c, FaceCard))
        tr = sum(c.value for c in self._hand if not isinstance(c, FaceCard))
        return te * tr

    def deal(self, deck: CardDeck) -> None:
        """This method deals a hand"""
        for _ in range(5):
            c = deck.deal()
            c.faceup = True
            self._hand.append(c)

    def return_to_deck(self, deck: CardDeck) -> None:
        """This method returns the hand cards to the deck"""
        while self._hand:
            deck.add(self._hand.pop())

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score


class TehiGame():
    """This class represents a Tehi Game"""
    def __init__(self):
        self._deck = CardDeck()
        self._gameswon = 0
        self._totalgames = 0
        self._besthandscore = 0
        self._playerhand = TehiHand()
        self._dealerhand = TehiHand()

    def __str__(self) -> str:
        return f'won {self._gameswon} of {self._totalgames} with best of {self._besthandscore}'

    def play(self) -> None:
        """This method plays a round of the game"""
        self._playerhand.return_to_deck(self._deck)
        self._dealerhand.return_to_deck(self._deck)
        self._deck.shuffle()
        self._playerhand.deal(self._deck)
        self._dealerhand.deal(self._deck)
        self._totalgames += 1
        self._besthandscore = max(self._playerhand.score, self._besthandscore)
        print(f'Player Hand {self._playerhand}, score {self._playerhand.score}')
        print(f'Dealer Hand {self._dealerhand}, score {self._dealerhand.score}')
        if self._dealerhand > self._playerhand:
            print('Dealer Wins!!')
        elif self._dealerhand < self._playerhand:
            print('Player Wins!!')
            self._gameswon += 1
        else:
            print('TIE!!')
        print(f'{self}')
        print()

if __name__ == "__main__":
    g = TehiGame()
    while True:
        action = input("What would you like to do? (p) Play, (n) New Deck (q) Quit ")
        match action:
            case 'p':
                g.play()
            case 'n':
                g = TehiGame()
            case 'q':
                break
