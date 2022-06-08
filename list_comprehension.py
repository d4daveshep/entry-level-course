# fill a list in one line

pawns = ["pawn" for i in range(8)]  # fill a list with the same item
print(pawns)

squares = [x ** 2 for x in range(10)]  # fill a list with a calculated item
print(squares)

odds = [x for x in squares if x % 2 != 0 ]  # fill the list with calculated values based on some criteria
print(odds)
