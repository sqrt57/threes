from enum import Enum, auto
import numbers

from threes.exceptions import InternalError
from threes.more_itertools import repeat_shuffles, immut_iter


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Card(Enum):
    EMPTY = 'empty'
    BONUS = 'bonus'
    C1 = 1
    C2 = 2
    C3 = 3
    C6 = 4
    C12 = 5
    C24 = 6
    C48 = 7
    C96 = 8
    C192 = 9
    C384 = 10
    C768 = 11
    C3072 = 12
    C6144 = 13
    C12288 = 14

    def is_empty(self):
        return self.value == self.EMPTY.value

    def not_empty(self):
        return self.value != self.EMPTY.value

    def is_bonus(self):
        return self.value == self.BONUS.value

    @classmethod
    def get_face_for(cls, num):
        if num <= 3:
            return num
        else:
            return 3 * 2**(num-3)

    @classmethod
    def get_score_for(cls, num):
        if num < 3:
            return 0
        else:
            return 3**(num-2)

    @property
    def face(self):
        if isinstance(self.value, numbers.Real):
            return self.get_face_for(self.value)
        elif isinstance(self.value, str):
            return self.value
        else:
            raise InternalError(
                "Unknown value type in Card enum: {}".format(self.value))

    @property
    def score(self):
        if isinstance(self.value, numbers.Real):
            return self.get_score_for(self.value)
        else:
            return 0


class Board:

    def __init__(self, *, width=4, height=4):
        self._width = width
        self._height = height
        self._board =\
            [[Card.EMPTY]*self._width for i in range(0, self._height)]

    def __getitem__(self, item):
        x, y = item
        return self._board[y][x]


class GameState:

    def __init__(self, *, board, deck):
        self._board = board
        self._deck = deck

    @property
    def board(self):
        return self._board

    @property
    def hint(self):
        return [self._deck.value]

    def make_move(self, move):
        pass


def new_game():
    rotation = [Card.C1, Card.C2, Card.C3] * 4
    deck = immut_iter(repeat_shuffles(rotation))
    return GameState(board=Board(), deck=deck)
