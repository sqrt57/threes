import random


def repeat_shuffles(values):
    v = list(values)
    while True:
        random.shuffle(v)
        yield from v


def select(selector, *seqs):
    iters = [iter(seq) for seq in seqs]
    for s in selector:
        yield next(iters[s])


class ImmutableIterator:

    def __init__(self, value, it):
        self._value = value
        self._it = iter(it)
        self._next = None

    def _force(self):
        if self._it is None:
            return
        try:
            value = next(self._it)
            self._next = ImmutableIterator(value, self._it)
        except StopIteration:
            self._next = None
        self._it = None

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        self._force()
        return self._next


def immut_iter(it):
    return ImmutableIterator(None, it).next
