from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards
from game_cards.CardGame import CardGame
from game_cards.Player import Player

player1 = Player(input("Enter name of player 1: "))
player2 = Player(input("Enter name of player 2: "))
this_game = CardGame(player1, player2)

# so that new_game couldn't be used in the main-USED_TO_BE_BUG
this_game.in_cardgame = False

print(this_game)

for i in range(10):
    print(f'Round {i+1}')
    player1_card = player1.get_card()
    player2_card = player2.get_card()
    if player1_card > player2_card:
        player1.add_card(player1_card)
        player1.add_card(player2_card)
        print(f"{player1.player_name} is the winner of this round!\n{player2.player_name}-card is: {player2_card} {player1.player_name}-card is: {player1_card}\n")
    elif player1_card == player2_card:
        if player1_card.card_suit > player2_card.card_suit:
            player1.add_card(player1_card)
            player1.add_card(player2_card)
            print(f"{player1.player_name} is the winner of this round!\n{player2.player_name}-card is: {player2_card} {player1.player_name}-card is: {player1_card}\n")
        else:
            player2.add_card(player1_card)
            player2.add_card(player2_card)
            print(f"{player2.player_name} is the winner of this round!\n{player2.player_name}-card is: {player2_card} {player1.player_name}-card is: {player1_card}\n")
    else:
            player2.add_card(player1_card)
            player2.add_card(player2_card)
            print(f"{player2.player_name} is the winner of this round!\n{player2.player_name}-card is: {player2_card} {player1.player_name}-card is: {player1_card}\n")

if this_game.get_winner() == None:
    print(f"It's a TIE, go cry to your MAMAs")
else:
    print(f"The Big WINNER of the Game is {this_game.get_winner()}")

