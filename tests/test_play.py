import unittest
import threes.play as play
import random

class TestDeck(unittest.TestCase):
    def setUp(self):
        random.seed(111)
        self.cards = [1,2,3,6,12,24,48,96,192,384,768,1536,3072,6144]

    def test_next(self):
        deck = play.Deck()
        card, next_deck = deck.next()
        self.assertIn(card, self.cards)

    def test_next_deck(self):
        deck = play.Deck()
        card, next_deck = deck.next()
        card1, next_deck1 = next_deck.next()
        self.assertIn(card1, self.cards)

    def test_cycle(self):
        expected = [1,1,1,1,2,2,2,2,3,3,3,3]
        obtained = []
        deck = play.Deck()
        for i in range(len(expected)):
            card, deck = deck.next()
            obtained.append(card)
        self.assertCountEqual(expected, obtained)

