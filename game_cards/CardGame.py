from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player

class CardGame:

    def __init__(self, player1:Player, player2:Player):
        """Function that gets the players' names, the number of their cards
        and calls the function new_game, which is described below"""
        self.player1 = player1
        self.player2 = player2
        self.in_cardgame= True
        self.new_game()

    def __str__(self):
        """Function that returns the message of the beginning of the game
        and contains the players' details"""
        return f"The game is about to start...\n"\
               f"Player 1: {self.player1}\n" \
               f"Player 2: {self.player2}\n" \
               f"May the force be with you!"

    def new_game(self):
        """Function that mixes the cards in the deck and gives them to each player"""
        if self.in_cardgame:
            deck = DeckOfCards()
            deck.cards_shuffle()
            self.player1.set_hand(deck)
            self.player2.set_hand(deck)
        else:
            print("Error! The function was not called from CardGame __init__")


    def get_winner(self):
        """Function that returns the player, which had gotten the biggest number of cards
        and won the game"""
        if len(self.player1.player_deck) > len(self.player2.player_deck):
            return self.player1
        elif len(self.player1.player_deck) < len(self.player2.player_deck):
            return self.player2
        else:
            return None

