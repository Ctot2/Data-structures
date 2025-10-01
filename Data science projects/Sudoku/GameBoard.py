
class GameBoard:
    game_board = []
    def __init__(self, game_board):
        self.board(game_board)


    def board(self, game_board):
        for i in range(9):
            #for j in range(9):
                game_board.append(["-"]*9)
        return game_board

    def print_board(self, game_board):
        for i in range(len(game_board)):
            print(" ".join([str(x) for x in game_board[i]]))


    def take_player_move(self, game_board):
        player_input = input("input move here: ")
        player_input2 = player_input.split()
        x = player_input2[0]
        y = player_input[1]
        z = player_input[3]

    def update_board(self, game_board, x, y, z):
        game_board[x][y] = z


