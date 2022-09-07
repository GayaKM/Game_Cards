from game_cards.Card import Card
import random
"""Import random in order to create a shuffle function below"""
class DeckOfCards:

    def __init__(self):
        """Function that sets an empty deck of cards and after that
        fills the deck with 52 cards according to the instructions"""
        self.deck_list=[]
        for i in range(1,5):
            for j in range(1,14):
                self.deck_list.append(Card(j,i))

    def __str__(self):
        """Function that allows to print the deck of cards"""
        return f"Deck of Cards {self.deck_list}"

    def cards_shuffle(self):
        """Function that reorganizes the deck of cards in a random order"""
        random.shuffle(self.deck_list)

    def deal_one(self):
        """Function that chooses one random card from the deck, removes it from there and returns the chosen card"""
        variant = random.choice(self.deck_list)
        self.deck_list.remove(variant)
        return variant

