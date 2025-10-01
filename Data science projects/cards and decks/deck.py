from cards import *
import random
class Deck:


    def __init__(self):
       self.cards = []
       for value in ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]:
           for suit in ["clubs", "diamonds", "hearts", "spades"]:
               self.cards.append(Card(value, suit))


    def __str__(self):
       list_of_cards = []
       for c in self.cards:
           list_of_cards.append(str(c))
       return "Deck contains: " + str(list_of_cards)

    def deck_length(self):
        return len(self.cards)

    def shuffle_deck(self):
       random.shuffle(self.cards)

    def add_card(self, c):
        self.cards.append(c)

    def flip_card(self):
        return self.cards.pop(0)


