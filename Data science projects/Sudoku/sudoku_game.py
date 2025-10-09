
class Sudoku:
    game_board = []
    is_game_over = False
    def __init__(self):
        self.game_board = self.create_board(game_board=[])
        self.is_game_over = False


    def create_board(self, game_board):
        for i in range(1):
                game_board.append([1, 2, 3, 4, 5, 6, 7, 8, "-"])
                game_board.append([2, 3, 4, 5, 6, 7, 8, 9, "-"])
                game_board.append([3, 4, 5, 6, 7, 8, 9, 1, "-"])
                game_board.append([4, 5, 6, 7, 8, 9, 1, 2, "-"])
                game_board.append([5, 6, 7, 8, 9, 1, 2, 3, "-"])
                game_board.append([6, 7, 8, 9, 1, 2, 3, 4, "-"])
                game_board.append([7, 8, 9, 1, 2, 3, 4, 5, "-"])
                game_board.append([8, 9, 1, 2, 3, 4, 5, 6,"-"])
        return game_board


    def print_board(self):
        for row in self.game_board:
            print(" ".join(map(str, row)))


    def take_player_move(self):
            player_input = list(map(int, input("Enter three integers separated by spaces: ").split()))
            x, y, z = player_input
            self.update_board(x, y, z)
            #return x, y, z


            #self.update_board(game_board, x, y, z)

    def update_board(self, x, y, z):
            self.game_board[x][y] = z

    def game_over(self):
        # Check if the game is over
        vertical_list1 = []
        for n in range (9):
            for i in range(9):
                    vertical_list1 = [row[n] for row in self.game_board]
                    if sorted([cell for cell in vertical_list1 if cell != "-"]) != list(range(1, 10)):
                        return False


        for row in self.game_board:
            if sorted([cell for cell in row if cell != "-"]) != list(range(1, 10)):
                return False

        print("you won!")
        return True





