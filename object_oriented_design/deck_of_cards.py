# Design a data structure for a generic deck of cards

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card(suit, rank))

    def print_cards(self):
        for card in self.cards:
            print(card)
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.suit == 0:
            suit = "Diamonds"
        elif self.suit == 1:
            suit = "Hearts"
        elif self.suit == 2:
            suit = "Spades"
        elif self.suit == 3:
            suit = "Clubs"

        r = self.rank + 1
        if r == 1:
            rank = "Ace"
        elif r == 11:
            rank = "Jack"
        elif r == 12:
            rank = "Queen"
        elif r == 13:
            rank = "King"
        else:
            rank = str(r)
        return rank + " of " + suit

    def __repr__(self):
        return self.__str__()

d = Deck()
d.print_cards()
