#from sudoku_game import *
#is_game_over = False
#game_board = []
#x = 0
#y = 0
#z = 0


#while not is_game_over:
    #my_sudoku = Sudoku(game_board)
    #my_sudoku.print_board(game_board)
    #my_sudoku.take_player_move(x, y, z, is_game_over= False)
    #my_sudoku.update_board(x, y, z)
    #my_sudoku.game_over(game_board, is_game_over = False)


    #from sudoku_game import *

from sudoku_game import *
is_game_over = False
game_board = []
x = 0
y = 0
z = 0

while not is_game_over:
    my_sudoku = Sudoku(game_board)
    my_sudoku.print_board(game_board)

    # Update x, y, z with the values returned from take_player_move
    x, y, z = my_sudoku.take_player_move(game_board, x, y, z, is_game_over = False)

    my_sudoku.update_board(x, y, z, game_board)
    is_game_over = my_sudoku.game_over(game_board, is_game_over= False)