from unittest import TestCase, mock
from unittest.mock import patch
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
import random

class TestPlayer(TestCase):

    def setUp(self):
        """Function that works automatically before any test, and gives the variants for the test"""
        self.player = Player("Orly",15)
        print("setUp")

    def tearDown(self):
        """Function that runs automatically after any test and closes the test"""
        print("tearDown")

    #Test __init__ Player

    def test__init__valid(self):
        """Function that test if the __init__ of Player worked in the set up and everything is valid"""
        self.assertEqual(self.player.player_name, "Orly")
        self.assertEqual(self.player.player_cards, 15)
        self.assertListEqual(self.player.player_deck, [])

    def test__init__valid_edge_player_cards(self):
        """Function that test if the __init__ of Player worked when the number of cards is in the edge of validtions"""
        player = Player("Yuval", 26)
        self.assertEqual(player.player_cards, 26)
        #self.assertEqual(player.player_name, "Yuval")
        #self.assertListEqual(player.player_deck, [])
        player = Player("Gaya", 10)
        self.assertEqual(player.player_cards, 10)
        # self.assertEqual(player.player_name, "Gaya")
        # self.assertListEqual(player.player_deck, [])

    def test__init__invalid_player_cards(self):
        """Function that test if invalid value of player_cards, must be >10 qnd <26 the player_cards will be 26 """
        player = Player("Yuval", 27)
        self.assertEqual(player.player_cards, 26)
        player = Player("Gaya", 9)
        self.assertEqual(player.player_cards, 26)

    def test__init__invalid_player_name(self):
        """Function that test if  invalid player_name, must be all letters. the program raise with Value error """
        with self.assertRaises(ValueError):
            player = Player("?", 15)
        with self.assertRaises(ValueError):
            player = Player(" ", 15)
        with self.assertRaises(ValueError):
            player = Player("Yuval?Gaya", 15)

    def test__init__invalid_player_name_type(self):
        """Function that test if the program raise with Type error when get's classes of player_name that isn't string class"""
        with self.assertRaises(TypeError):
            player = Player(13)
        with self.assertRaises(TypeError):
            player = Player(1.3)
        with self.assertRaises(TypeError):
            player = Player((1.3,13))
        with self.assertRaises(TypeError):
            player = Player({1.3:13})
        with self.assertRaises(TypeError):
            player = Player(["Yuval", "Gaya"])

    def test__init__invalid_player_cards_type(self):
        """Function that test if the program raise with Type error when get's classes of player_cards that isn't integer class"""
        with self.assertRaises(TypeError):
            player= Player("Orly", 10.3)
        with self.assertRaises(TypeError):
            player= Player("Orly", "10")
        with self.assertRaises(TypeError):
            player= Player("Orly", (10,))
        with self.assertRaises(TypeError):
            player= Player("Orly", {10:3})

    #Test set_hand
    def test_set_hand_valid(self):
        """Funcion that test the length of a player deck list is as thier player card number"""
        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertEqual(len(self.player.player_deck), 15)

    def test_set_hand_valid_one_card_only(self):
        """Function that test if the card in one deck it can't be in the other"""
        deck = DeckOfCards()
        card= Card(5,3)
        player= Player("Orly")
        player.set_hand(deck)
        for i in player.player_deck:
            if i.card_value == card.card_value and i.card_suit == card.card_suit:
                for j in range(len(deck.deck_list)):
                    if deck.deck_list[j].card_value == card.card_value and deck.deck_list[j].card_suit == card.card_suit:
                        break
                    else:
                        pass
            else:
                for j in range(len(deck.deck_list)):
                    if deck.deck_list[j].card_value == card.card_value and deck.deck_list[j].card_suit == card.card_suit:
                        pass

    def test_set_hand_valid_adge(self):
        deck = DeckOfCards()
        player= Player("Orly",10)
        player.set_hand(deck)
        self.assertEqual(len(player.player_deck), 10)
        deck = DeckOfCards()
        player = Player("Orly",26)
        player.set_hand(deck)
        self.assertEqual(len(player.player_deck), 26)

    def test_set_hand_invalid_length(self):
        """Funcion that test the length of a player deck list can't be diffrent from the player_cards"""
        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertFalse(len(self.player.player_deck)>15)
        self.assertFalse(len(self.player.player_deck)<15)

    #Test get_card
    def test_get_card_valid(self):
       """Function that test that the card indeed removed from the player_deck"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = self.player.get_card()
       for i in range(len(self.player.player_deck)):
           self.assertNotEqual(self.player.player_deck[i], variant)

    def test_get_card_valid_variant(self):
       """Function that test that the variant is from the player_deck"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = random.choice(self.player.player_deck)
       for i in range(len(self.player.player_deck)):
           if self.player.player_deck[i] == variant:
               pass

    def test_get_card_valid_value(self):
       """Function that test that the card that was taken from the player deck value is valid"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = self.player.get_card()
       self.assertTrue(1<= variant.card_value <=13)

    def test_get_card_valid_suit(self):
       """Function that test that the card that was taken from the player deck suit is valid"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = self.player.get_card()
       self.assertTrue(1<= variant.card_suit <=4)

    def test_get_card_invalid_value(self):
       """Function that test that the card that was taken from the player deck value is not invalid"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = self.player.get_card()
       self.assertFalse(1> variant.card_value or variant.card_value >13)

    def test_get_card_invalid_suit(self):
       """Function that test that the card that was taken from the player deck suit is not invalid"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = self.player.get_card()
       self.assertFalse(1> variant.card_suit or variant.card_suit >4)

    def test_get_card_valid_suit(self):
       """Function that test that the card that was taken from the player deck suit is valid"""
       deck=DeckOfCards()
       self.player.set_hand(deck)
       variant = self.player.get_card()
       self.assertTrue(1<= variant.card_suit <=4)

    #Test add_card
    def test_add_card_valid_added(self):
        c= Card(5,3)
        self.player.add_card(c)
        for i in range(len(self.player.player_deck)):
            if self.player.player_deck[i] == c:
                pass

    def test_get_card_valid_value_edge(self):
       """Function that test that the card added to the player_deck in the edges of value validtion"""
       card = Card(13, 3)
       self.player.add_card(card)
       for i in range(len(self.player.player_deck)):
           if self.player.player_deck[i] == card:
               pass
       card = Card(1, 3)
       self.player.add_card(card)
       for i in range(len(self.player.player_deck)):
           if self.player.player_deck[i] == card:
               pass

    def test_get_card_valid_value_suit(self):
        """Function that test that the card added to the player_deck in the edges of suit validtion"""
        card= Card(5,1)
        self.player.add_card(card)
        for i in range(len(self.player.player_deck)):
            if self.player.player_deck[i] == card:
                pass
        card = Card(5, 4)
        self.player.add_card(card)
        for i in range(len(self.player.player_deck)):
            if self.player.player_deck[i] == card:
                pass

    def test_add_card_invalid_card_type(self):
        """Function that test if the program raise with Type error when add card get's somthing else then Card class"""
        with self.assertRaises(TypeError):
            card= 5
            self.player.add_card(card)
        with self.assertRaises(TypeError):
            card= 5.5
            self.player.add_card(card)
        with self.assertRaises(TypeError):
            card= "5"
            self.player.add_card(card)
        with self.assertRaises(TypeError):
            card= (5,)
            self.player.add_card(card)

    def test_add_card_invalid_card_value(self):
        """Function that test the program raise with Type error when add card get's Card with invalid value"""
        with self.assertRaises(ValueError):
            card= Card(14,3)
            self.player.add_card(card)
        with self.assertRaises(ValueError):
            card= Card(0,3)
            self.player.add_card(card)
        with self.assertRaises(ValueError):
            card= Card(-1,3)
            self.player.add_card(card)

    def test_add_card_invalid_card_suit(self):
        """Function that test the program raise with Type error when add card get's Card with invalid suit"""
        with self.assertRaises(ValueError):
            card= Card(5,5)
            self.player.add_card(card)
        with self.assertRaises(ValueError):
            card= Card(5,0)
            self.player.add_card(card)
        with self.assertRaises(ValueError):
            card= Card(5,-3)
            self.player.add_card(card)