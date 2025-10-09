
from sudoku_game import *


my_sudoku = Sudoku()
while not my_sudoku.is_game_over:
    my_sudoku.print_board()
    my_sudoku.take_player_move()
    my_sudoku.is_game_over = my_sudoku.game_over()