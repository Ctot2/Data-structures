from TwentyQuestions import *
class Node:

    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None

    def set_left(self, n):
        self.left_child = n

    def set_right(self,n):
        self.right_child = n

    def set_value(self, val):
        self.value = val

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def get_value(self):
        return self.value

    def is_leaf(self):
        if self.get_left() is None:
            if self.get_right() is None:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        s = "{" + str(self.get_value())
        if self.get_left() != None:
            s = s + ", Left: " + str(self.get_left())
        if self.get_right() != None:
            s = s + ", Right: " + str(self.get_right())
        s = s + "}"
        return s

class BinaryTree:

    def __init__(self, n):
        self.root = n

    def get_root(self):
        return self.root

    def __str__(self):
        return "Tree: " + str(self.get_root())

    def yes_or_no():
        a = input("input here: ")
        if a == "yes":
            return True
        elif a == "no":
            return False
        else:
            print("enter yes or no")
            return yes_or_no()

    def play_game(self):
        temp = self.get_root()
        print(temp.get_value())
        while temp.is_leaf() is False:
            temp2 = yes_or_no()
            if temp2 == True:
                temp = temp.get_left()
                print(temp.get_value())
            elif temp2 ==  False:
                temp = temp.get_right()
                print(temp.get_value())
        print(temp)
        self.adaptive(temp = temp)

    def adaptive(self, temp):
        print(temp)
        print("was this guess correct?")
        if  yes_or_no() == True:
            print("play again?")
            if yes_or_no() == True:
                self.play_game()
            else:
                print(self)
                exit()
        else:
            other_answer = temp
            print(other_answer)
            player_guess = input("what were you thinking of?")
            player_question = input("what question could i have asked to figure it out?")
            print("would you have answered yes or no to that question?")
            player_answer = yes_or_no()
            temp.set_value(player_question)
            if player_answer == True:
                temp.set_left(Node(player_guess))
                temp.set_right(Node(other_answer))
            else:
                temp.set_right(Node(player_guess))
                temp.set_left(Node(other_answer))
        self.play_game()