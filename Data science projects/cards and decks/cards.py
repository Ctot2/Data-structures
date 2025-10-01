class Card:


   def __init__(self, v, s):
       self.value = v
       self.suit = s


   def __str__(self):
       return self.value + " of " + self.suit

   def get_rank(self):
       card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
       return card_values.index(self.value)
