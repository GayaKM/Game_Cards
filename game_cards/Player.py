from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
import random
"""Import random in order to create a get_card function below"""

class Player:

    def __init__(self, name, number_of_cards=26):
        """Function that receives a name of a player and a number of cards
        which is 26 by default. The method also initializes the deck of cards as
        an empty list for every player and also makes sure the name of the players is of string class
        and the number of cards is of integer class by calling the appropriate functions (below)"""
        if type(name) != str:
            raise TypeError("Invalid name: must be of string class")
        if type(number_of_cards) != int:
            raise TypeError("Invalid number: must be of integer class")
        #chack that the name is only letters- -USED_TO_BE_BUG
        if name.isalpha() == False:
            raise ValueError("Player name must be only letters")

        self.player_name = name
        self.player_deck = []
        if number_of_cards < 10 or number_of_cards > 26:
            self.player_cards = 26
        else:
            self.player_cards = number_of_cards

    def __repr__(self):
        """Function that returns a Player name and the player's deck of cards"""
        return f"{self.player_name}, your deck of cards is {self.player_deck}"

    def set_hand(self,deck:DeckOfCards):
        """Function that receives a deck of cards and gives random cards to every player
        according to the amount, which the players have to receive"""
        for i in range(self.player_cards):
            self.player_deck.append(deck.deal_one())

    def get_card(self):
        """Function that gets a random card from the player's deck and removes it from deck.
        The function returns the chosen card"""
        variant = random.choice(self.player_deck)
        self.player_deck.remove(variant)
        return variant

    def add_card(self,card:Card):
        """Function that receives a card and adds it to the deck of player"""
        #chack that it's indeed card type-ADD_TO_BE_GLOBAL
        if type(card) != Card:
            raise TypeError("Invalid card: must be of Card class")

        self.player_deck.append(card)
