from card import Card
from deck import Deck
import unittest

class CardTest(unittest.TestCase) :
    def setUp(self) :
        self.card = Card("A","Hearts")
    def test_init(self) :
        """Cards should have a suit and a value"""
        self.assertEqual(self.card.value, "A")
        self.assertEqual(self.card.suit, "Hearts")

    def test_repr(self) :
        """repr should return a string of the form """
        self.assertEqual(repr(self.card), "A of Hearts")

class DeckTest(unittest.TestCase) :

    def setUp(self):
        self.deck = Deck()

    def test_count(self) :
        """count should return a count of the number of cards in the deck """
        self.assertEqual(self.deck.count(), len(self.deck.cards))

    def test_deal_card(self) :
        """deal_card should deal a single card from the deck """
        self.assertIsInstance(self.deck.deal_card(),Card)

    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed into it """
        self.assertEqual(len(self.deck.deal_hand(5)),5)

    def test_deal_insufficient_cards(self):
        """ deal should deal the number of cards
        left in the deck, if more card are requsted"""
        self.assertEqual(self.deck._deal(53)," 52 missing card 1" )

    def test_deal_no_cards(self):
        """should throw value error if the deck is empty"""
        with self.assertRaises(ValueError) as context :
            self.deck.deal_hand(52)
            self.deck.deal_card()

        self.assertTrue("All cards have been dealt" in str(context.exception))
    def test_deal_sufficient_cards(self):
        """deal should deal the nummber of cards specified if possible"""
        self.assertTrue(self.deck._deal(2),2 is int)

    def test_repr(self):
        """deck should have 52 cards"""
        self.assertEqual(str(self.deck), "Deck of 52 cards")

    def test_init(self):
        """deck as 52 element list """
        self.assertEqual(len(self.deck.cards),52)

    def  test_deck_shuffle_full_deck(self):
        """ shudle shuffle the deck if the deck is full """
        self.assertTrue(self.deck.shuffle(),self.deck.count() == 52)

    def  test_deck_shuffleNot_full_deck(self):
        """ shudle shuffle the deck if the deck is not full """
        self.assertTrue(self.deck.shuffle(),self.deck.count() !=  2)









if __name__ == "__main__":
    unittest.main()
