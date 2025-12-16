score_map = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}

dummy_input = """A Y
B X
C Z"""


class Move:
    gt = ""
    lt = ""
    eq = ""

    def __gt__(self, __o):
        if __o.__class__.__name__.lower() == self.gt:
            return True
        return False

    def __lt__(self, __o):
        if __o.__class__.__name__.lower() == self.lt:
            return True
        return False

    def __eq__(self, __o: object) -> bool:
        if __o.__class__.__name__.lower() == self.eq:
            return True
        return False


class Rock(Move):
    value = 1
    code = "A"
    gt = "scissors"
    lt = "paper"
    eq = "rock"


class Paper(Move):
    value = 2
    code = "B"
    gt = "rock"
    lt = "scissors"
    eq = "paper"


class Scissors(Move):
    value = 3
    code = "C"
    gt = "paper"
    lt = "rock"
    eq = "scissors"


def move_factory(move):
    if move in ("A", "X"):
        return Rock()
    elif move in ("B", "Y"):
        return Paper()
    elif move in ("C", "Z"):
        return Scissors()


def main_1():
    my_score = 0
    with open("input.txt") as f:
        scores = f.readlines()
        scores = [i.strip("\n") for i in scores]
    scores = [a.split(" ") for a in scores]
    for i in scores:
        a, b = move_factory(i[0]), move_factory(i[1])
        my_score = update_score(a, b, my_score)
    print(my_score)


expected_result = {"X": "__lt__", "Y": "__eq__", "Z": "__gt__"}


def update_score(my_move, opponent_move, my_score) -> Scissors | Rock | Paper:
    if my_move == opponent_move:
        my_score += 3 + score_map[my_move.code]
    elif my_move < opponent_move:
        my_score += score_map[my_move.code]
    else:
        my_score += score_map[my_move.code] + 6
    return my_score


def get_expected(expected: str, other: Rock | Paper | Scissors):
    for move_type in ["A", "B", "C"]:
        move = move_factory(move_type)
        func = getattr(move, expected_result[expected])
        if func(other):
            return move


def main_2():
    my_score = 0
    with open("input.txt") as f:
        scores = f.readlines()
        scores = [i.strip("\n") for i in scores]
    scores = [a.split(" ") for a in scores]
    for score in scores:
        opponent_move = move_factory(score[0])
        expected_move = get_expected(score[1], opponent_move)
        my_score = update_score(expected_move, opponent_move, my_score)
    print(my_score)