from unittest import TestCase
from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards
from game_cards.CardGame import CardGame
from game_cards.Player import Player
# from unittest.mock import patch


class TestCardGame(TestCase):

    def setUp(self):
        """Function that works automatically before any test and gives the variants for the test"""
        self.player1 = Player("Yuval",25)
        self.player2 = Player("Gaya",15)
        self.card_game1 = CardGame(self.player1, self.player2)
        print("setUp")

    def tearDown(self):
        """Function that runs automatically after any test and closes the test"""
        print("tearDown")

    # Test __init__function
    def test__init__valid_name(self):
        """Makes sure that the valid player name, that was received by the Player object, is the same one"""
        self.assertEqual("Yuval", self.player1.player_name)
        self.assertEqual("Gaya", self.player2.player_name)

    def test__init__valid_deck_of_cards(self):
        """Makes sure that the valid number of cards, that was received by the Player object, is the same one"""
        self.assertEqual(25, self.player1.player_cards)
        self.assertEqual(15, self.player2.player_cards)

    def test__init__boundary_values_deck_of_cards(self):
        """Checks whether the boundary values of number of cards are valid"""
        self.player1 = Player("Yuval", 26)
        self.player2 = Player("Gaya", 10)
        self.assertEqual(26, self.player1.player_cards)
        self.assertEqual(10, self.player2.player_cards)

    def test__init__invalid_values_1(self):
        """Checks if the number of cards is between 10 and 26, and if it is more than 26
        the function will use the default of 26 cards"""
        self.player1 = Player("Yuval", 27)
        self.assertEqual(26, self.player1.player_cards)

    def test__init__invalid_values_2(self):
        """Checks if the number of cards is between 10 and 26, and if it is less than 10
        the function will use the default of 26 cards"""
        self.player2 = Player("Gaya", 9)
        self.assertEqual(26, self.player2.player_cards)

    def test_init_invalid_name1(self):
        """Makes sure the exception handling works properly"""
        with self.assertRaises(TypeError):
            player1 = Player({50:40})

    def test_init_invalid_name2(self):
        """Makes sure the exception handling works properly"""
        with self.assertRaises(TypeError):
            player2 = Player(7,15)
            self.assertEqual(7,self.player1.player_name)

    def test_init_invalid_name3(self):
        """Makes sure the exception handling works properly"""
        with self.assertRaises(TypeError):
            self.player1 = Player({"yu":"val"},26)
            self.assertEqual({"yu":"val"},self.player1.player_name)

    def test__init__valid1(self):
        """Makes sure the boolean variable returns True"""
        self.assertTrue(self.card_game1.in_cardgame)


    def test_new_game_shuffle(self):
        """Checks whether new_game function uses shuffle function"""
        deck = DeckOfCards()
        player1 = Player("Yuval")
        player2 = Player("Gaya")
        game = CardGame(player1,player2)
        game.in_cardgame = True
        self.assertNotEqual(deck.cards_shuffle(),deck)

    def test_new_game_invalid(self):
        deck = DeckOfCards()
        player1 = Player("Yuval",10)
        player2 = Player("Gaya",10)
        game = CardGame(player1, player2)
        game.in_cardgame = False
        self.assertNotEqual(deck.cards_shuffle(), deck)

    def test_new_game_set_hand(self):
        """Checks whether the players' decks of cards are different (and not the same)"""
        deck = DeckOfCards()
        player1 = Player("Yuval", 10)
        player2 = Player("Gaya", 10)
        game = CardGame(player1, player2)
        game.in_cardgame = False
        player1.set_hand(deck)
        player2.set_hand(deck)
        self.assertNotEqual(player1.player_deck,player2.player_deck)

    def test_get_winner(self):
        """Checks if the function get winner returns the right player"""
        deck = DeckOfCards()
        player1 = Player("Yuval", 10)
        player2 = Player("Gaya", 10)
        game = CardGame(player1, player2)
        game.in_cardgame = False
        player1.player_deck = 30
        player2.player_deck = 22
        self.assertGreater(player1.player_deck,player2.player_deck)
        player2.player_deck = 30
        player1.player_deck = 22
        self.assertGreater(player2.player_deck, player1.player_deck)
        player2.player_deck = 26
        player1.player_deck = 26
        self.assertEqual(player2.player_deck, player1.player_deck)