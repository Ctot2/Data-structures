from binarytree import *
n1 = Node("does it have 4 legs? ")
n1.set_left(Node("does it have pointy ears? "))
n1.get_left().set_left(Node("cat"))
n1.get_left().set_right(Node("dog"))
n1.set_right(Node("can it swim? "))
n1.get_right().set_left(Node("fish"))
n1.get_right().set_right(Node("bird"))
game_tree = BinaryTree(n1)


game_tree.play_game()
