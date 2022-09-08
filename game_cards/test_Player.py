from unittest import TestCase, mock
from unittest.mock import patch
from Player import Player


class TestPlayer(TestCase):

    def setUp(self):
        """Function that works automatically before any test, and gives the variants for the test"""
        self.player = Player("Yuval the King",15)
        print("setUp")

    def tearDown(self):
        """Function that runs automatically after any test and closes the test"""
        print("tearDown")

        # Test __init__ Card

    def test__init__valid(self):