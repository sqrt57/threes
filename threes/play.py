import random

class Deck(object):
    def __init__(self, cycle=None):
        if cycle is None:
            self.cycle = [1,1,1,1,2,2,2,2,3,3,3,3]
            random.shuffle(self.cycle)
        else:
            self.cycle = cycle

    def next(self):
        card = self.cycle[0]
        rest = self.cycle[1:]
        return card, Deck(rest)
