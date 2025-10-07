
class Sudoku:
    game_board = []
    is_game_over = False
    def __init__(self, game_board):
        self.board(game_board)


    def board(self, game_board):
        for i in range(9):
                game_board.append(["-"]*9)
        return game_board

    def print_board(self, game_board):
        for i in range(len(game_board)):
            print(" ".join([str(x) for x in game_board[i]]))


    def take_player_move(self, game_board, x, y, z, is_game_over):
            player_input = list(map(int, input("Enter three integers separated by spaces: ").split()))
            x = player_input[0]
            y = player_input[1]
            z = player_input[2]

            game_board[x][y] = z
            return x, y, z


            #self.update_board(game_board, x, y, z)

    def update_board(self, game_board, x, y, z):
            game_board[x][y] = z

    def game_over(self, game_board, is_game_over):
        for i in range(9):
                if 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9 in game_board[i]:
                    is_game_over = True
                    self.take_player_move(game_board, is_game_over)



