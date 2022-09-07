"""Class that has a description of every card in the game"""
class Card:
    """Every card has two properties: a value and a suit"""
    def __init__(self,value,suit):
        # chack that value and suit are in their range -USED_TO_BE_BUG
        if 1>value or value>13:
            raise ValueError("Invalid card value: must be between 1-13 (includes)")
        if 1>suit or suit>4:
            raise ValueError("Invalid card suit: must be between 1-4 (includes)")

        # chack that value and suit are Integer class -ADDED_TO_BE_GLOBAL
        if type(value) != int:
            raise TypeError("Invalid card value: must be of integer class")
        if type(suit) != int:
            raise TypeError("Invalid suit value: must be of integer class")

        self.card_value = value
        self.card_suit = suit

    def __repr__(self):
        """Function that allows to print card's properties"""
        return f"The card's value is {self.value_name()} of {self.suit_name()}"


    def __gt__(self, other):
        """Function that checks cards' values in order to find the grater one.
        If the values are equal, it returns None"""
        # chack that other is a Card class -ADDED_TO_BE_GLOBAL
        if type(other) != Card:
            raise TypeError("Invalid variant: must be of Card class")

        if self.card_value>other.card_value and other.card_value != 1:
            return True
        elif self.card_value == 1 and other.card_value != 1:
            return True
        else:
            return False

    def __eq__(self, other):
        """Function that compares cards' values in order to determine whether they are equal"""
        # chack that other is a Card class -ADDED_TO_BE_GLOBAL
        if type(other) != Card:
            raise TypeError("Invalid variant: must be of Card class")

        if self.card_value == other.card_value:
            return True
        else:
            return False

    def suit_name(self):
        """An additional function that returns a suit name of every card's value"""
        if self.card_suit == 1:
            return f"Diamond"
        elif self.card_suit == 2:
            return f"Spade"
        elif self.card_suit == 3:
            return f"Heart"
        elif self.card_suit == 4:
            return f"Club"

    def value_name(self):
        """An additional function that returns special value names (Ace, Jack, Queen, King)"""
        if self.card_value == 1:
            return f"Ace"
        elif self.card_value == 11:
            return f"Jack"
        elif self.card_value == 12:
            return f"Queen"
        elif self.card_value == 13:
            return f"King"
        else:
            return str(self.card_value)


