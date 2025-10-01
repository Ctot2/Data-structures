def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))


checkerboard = []


for i in range(8):
   if i < 3 or i > 4:
       if i % 2 == 1:
           checkerboard.append([0, 1, 0, 1, 0, 1, 0, 1])
       else:
           checkerboard.append([1, 0, 1, 0, 1, 0, 1, 0])
   else:
       checkerboard.append([0]*8)

print_board(checkerboard)
