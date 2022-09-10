from unittest import TestCase
from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards
import random
# from unittest import TestCase, mock
# from unittest.mock import patch

class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck_list = DeckOfCards()
        """Function that works automatically before any test and gives the variants for the test"""
        print("setUp")

    def tearDown(self):
        """Function that runs automatically after any test and closes the test"""
        print("tearDown")

    # Test __inint__DeckOfCards:
    def test_init_valid_deck(self):
        """Makes sure that the smaller card is placed on the first index in the deck"""
        self.card = Card(1,1)
        self.assertEqual(self.deck_list.deck_list[0],self.card)


    def test_init_number_of_cards_in_the_deck(self):
        """Makes sure the deck of cards has exactly 52 cards"""
        self.deck_list = DeckOfCards()
        self.assertEqual(len(self.deck_list.deck_list), 52)

    def test_cards_shuffle1(self):
        """Checks if the instance of the deck had changed after shuffle function"""
        deck = DeckOfCards()
        deck.cards_shuffle()
        self.assertIsInstance(deck,DeckOfCards)

    def test_cards_shuffle2(self):
        """Checks if the number of cards in the deck had changed after shuffle function"""
        deck = DeckOfCards()
        len_of_deck = len(deck.deck_list)
        deck.cards_shuffle()
        self.assertEqual(len(deck.deck_list), len_of_deck)


    def test_deal_one_valid(self):
        """Checks whether the randomly chosen and removed from the deck card does not appear in the deck"""
        deck = DeckOfCards()
        card = random.choice(deck.deck_list)
        deck.deck_list.remove(card)
        self.assertNotIn(card,deck.deck_list)