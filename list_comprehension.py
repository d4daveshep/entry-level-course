# fill a list in one line

pawns = ["pawn" for i in range(8)]  # fill a list with the same item
print(pawns)

squares = [x ** 2 for x in range(10)]  # fill a list with a calculated item
print(squares)

odds = [x for x in squares if x % 2 != 0 ]  # fill the list with calculated values based on some criteria
print(odds)

# create a 2D list array
board = [["-" for i in range(8)] for j in range(8)]  # this is very cool use of nexted list comprehension
print(board)

# create a chess board and place rooks in corners
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

