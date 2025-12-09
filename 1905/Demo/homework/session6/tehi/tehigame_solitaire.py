"""This is an implementation of The Eyes Have It Solitaire"""
from cardlib import FaceCard, CardDeck

class TehiGame():
    """This class represents a Tehi Game"""
    def __init__(self):
        self._deck = CardDeck()
        self._hand = []
        self._handsdealt = 0
        self._besthandscore = 0

    def __str__(self) -> str:
        return " ".join(str(card) for card in self._hand)

    def deal(self) -> None:
        """This method deals a hand"""
        while len(self._hand) > 0:
            c = self._hand.pop()
            self._deck.add(c)
        self._deck.shuffle()
        for _ in range(5): # pylint: disable=W0612
            c = self._deck.deal()
            c.faceup = True
            self._hand.append(c)
        self._handsdealt += 1
        self._besthandscore = max(self.score, self._besthandscore)

    @property
    def score(self) -> int:
        """This property calculates the score of a hand"""
        te = sum(c.eyes for c in self._hand if isinstance(c, FaceCard))
        tr = sum(c.value for c in self._hand if not isinstance(c, FaceCard))
        return te * tr

    @property
    def handsdealt(self) -> int:
        """This method returns the number of hands dealt"""
        return self._handsdealt

    @property
    def besthandscore(self) -> int:
        """This method returns the best score on a hand"""
        return self._besthandscore

if __name__ == "__main__":
    g = TehiGame()
    while True:
        action = input("What would you like to do? (d) Deal, (n) New Deck (q) Quit ")
        match action:
            case 'd':
                g.deal()
                print(f'hand {g}')
                print(f'score={g.score}, best={g.besthandscore} of {g.handsdealt} hands')
            case 'n':
                g = TehiGame()
            case 'q':
                break
