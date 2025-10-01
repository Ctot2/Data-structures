from cards import *
from deck import *


#my_card = Card("7", "clubs")
#print(my_card)


my_deck = Deck()
my_deck.shuffle_deck()
my_deck2 = Deck()
my_deck2.shuffle_deck()

while True:
    if len(my_deck.cards) == 0:
        print("overall winner: player 2")
        exit()
    elif len(my_deck2.cards) == 0:
        print("overall winner: player 1")
        exit()
    else:
        card = my_deck.flip_card()
        card2 = my_deck2.flip_card()
        print("player 1's card: ", card, "player 2's card:",  card2)
        if card.get_rank() > card2.get_rank():
            print("player 1 wins")
            my_deck.add_card(card)
            my_deck.add_card(card2)
        elif card2.get_rank() > card.get_rank():
            print("player 2 wins")
            my_deck2.add_card(card2)
            my_deck2.add_card(card)
        else:
            card3 = my_deck.flip_card()
            print(card3)
            card4 = my_deck2.flip_card()
            print(card4)
            if card3.get_rank() > card4.get_rank():
                print("player 1 wins")
                my_deck.add_card(card)
                my_deck.add_card(card2)
                my_deck.add_card(card3)
                my_deck.add_card(card4)
            elif card4.get_rank() > card3.get_rank():
                print("player 2 wins")
                my_deck2.add_card(card2)
                my_deck2.add_card(card4)
                my_deck2.add_card(card)
                my_deck2.add_card(card3)
            else:
                card5 = my_deck.flip_card()
                print(card5)
                card6 = my_deck2.flip_card()
                print(card6)
                if card5.get_rank() > card6.get_rank():
                    print("player 1 wins")
                    my_deck.add_card(card)
                    my_deck.add_card(card3)
                    my_deck.add_card(card5)
                    my_deck.add_card(card2)
                    my_deck.add_card(card4)
                    my_deck.add_card(card6)
                elif card6.get_rank() > card5.get_rank():
                    print("player 2 wins")
                    my_deck2.add_card(card2)
                    my_deck2.add_card(card4)
                    my_deck.add_card(card6)
                    my_deck2.add_card(card)
                    my_deck2.add_card(card3)
                    my_deck.add_card(card5)
                else:
                    print("both players get struck by lightning")
                    exit()