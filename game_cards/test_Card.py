from unittest import TestCase, mock
from unittest.mock import patch
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        """Function that works automatically before any test, and gives the variants for the test"""
        self.card=Card(5,3)
        print("setUp")

    def tearDown(self):
        """Function that runs automatically after any test and closes the test"""
        print("tearDown")

   #Test __init__ Card
    def test__init__valid(self):
        """Function that test if the __init__ of Card worked in the set up and the values and suits are valid"""
        self.assertEqual(self.card.card_value, 5)
        self.assertEqual(self.card.card_suit, 3)

    def test__init__valid_edge_value(self):
        """Function that test if the __init__ of Card worked when the values are in the edge of validtions"""
        card=Card(1,2)
        self.assertEqual(card.card_value, 1)
        self.assertEqual(card.card_suit, 2)
        card = Card(13, 3)
        self.assertEqual(card.card_value, 13)
        self.assertEqual(card.card_suit, 3)

    def test__init__valid_edge_suit(self):
        """Function that test if the __init__ of Card worked when the suits are in the edge of validtions"""
        card=Card(2,1)
        self.assertEqual(card.card_value, 2)
        self.assertEqual(card.card_suit, 1)
        card = Card(12, 4)
        self.assertEqual(card.card_value, 12)
        self.assertEqual(card.card_suit, 4)

    def test__init__invalid_values(self):
        """Function that test if the program raise with Value error when get's invalid card Values"""
        with self.assertRaises(ValueError):
            card = Card(14, 2)
        with self.assertRaises(ValueError):
            card = Card(0, 2)
        with self.assertRaises(ValueError):
            card = Card(-13, 2)
        with self.assertRaises(ValueError):
            card = Card(100, 2)

    def test__init__invalid_suits(self):
        """Function that test if the program raise with Value error when get's invalid card Suits"""
        with self.assertRaises(ValueError):
            card = Card(12, 5)
        with self.assertRaises(ValueError):
            card = Card(3, 0)
        with self.assertRaises(ValueError):
            card = Card(12, -4)
        with self.assertRaises(ValueError):
            card = Card(3, 100)

    def test__init__invalid_value_type(self):
        """Function that test if the program raise with Type error when get's classes of card Value that isn't integer"""
        with self.assertRaises(TypeError):
            card = Card("13", 2)
        with self.assertRaises(TypeError):
            card = Card(1.5, 2)
        with self.assertRaises(TypeError):
            card = Card("?", 2)
        with self.assertRaises(TypeError):
            card = Card([1,2,3,4], 2)
        with self.assertRaises(TypeError):
            card = Card((1,2,3,4), 2)

    def test__init__invalid_value_suite(self):
        """Function that test if the program raise with Type error when get's classes of card Suits that isn't integer"""
        with self.assertRaises(TypeError):
            card = Card(10, "2")
        with self.assertRaises(TypeError):
            card = Card(10, 2.2)
        with self.assertRaises(TypeError):
            card = Card(10, "<3")
        with self.assertRaises(TypeError):
            card = Card(10, {1:2, 3:4})
        with self.assertRaises(TypeError):
            card = Card(10, [2,2,3])


    def test_suit_name(self):
        self.fail()

    def test_value_name(self):
        self.fail()
