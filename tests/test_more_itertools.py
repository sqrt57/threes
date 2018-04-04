import itertools
from unittest import TestCase

from threes import more_itertools

class TestMoreItertools(TestCase):

    def test_repeat_shuffles(self):
        values = [1, 2, 2]
        result = iter(more_itertools.repeat_shuffles(values))
        a1 = next(result)
        a2 = next(result)
        a3 = next(result)
        b1 = next(result)
        b2 = next(result)
        b3 = next(result)
        self.assertCountEqual([a1, a2, a3], [1, 2, 2])
        self.assertCountEqual([b1, b2, b3], [1, 2, 2])

    def test_select(self):
        selector = [0, 1, 0, 2]
        list0 = ['a', 'b', 'c']
        list1 = ['q', 'w', 'e']
        list2 = [1, 2, 3]
        result = list(more_itertools.select(selector, list0, list1, list2))
        self.assertEqual(result, ['a', 'q', 'b', 1])

    def test_immutable_iterator(self):
        l = [1, 2]
        it = more_itertools.immut_iter(l)
        self.assertEqual(it.value, 1)
        self.assertEqual(it.next.value, 2)
        self.assertIsNone(it.next.next)

    def test_immutable_iterator_empty(self):
        l = []
        it = more_itertools.immut_iter(l)
        self.assertIsNone(it)

    def test_immutable_iterator_infinite(self):
        l = itertools.repeat(1)
        it = more_itertools.immut_iter(l)
        self.assertEqual(it.value, 1)
        self.assertEqual(it.next.value, 1)
