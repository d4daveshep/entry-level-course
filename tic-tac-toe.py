def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    draw_divider = "+-------+-------+-------+"
    draw_spacer = "|       |       |       |"
    for i in range(board_size):
        print(draw_divider)
        print(draw_spacer)
        for j in range(board_size):
            print("|   ", board[i][j], "   ", sep="", end="")
        print("|")
        print(draw_spacer)
    print(draw_divider)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    chars = computer_char + player_char
    for i in range(board_size):
        for j in range(board_size):
            contents = board[i][j]
            if contents in chars:
                continue
            free_fields.append((i, j))
    return free_fields


def draw_move(board):
    # The function draws the computer's move and updates the board.
    if board[1][1] == "5":
        board[1][1] = computer_char
    # else:
    #     print(make_list_of_free_fields(board))


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    free_spaces = make_list_of_free_fields(board)
    valid_moves = ""
    for space in free_spaces:
        valid_moves += board[space[0]][space[1]]
    print("Valid moves are", valid_moves)
    player_move = "."
    while (player_move not in valid_moves):
        player_move = input("Enter your move...")  # TODO: exception handling needed
    index = valid_moves.find(player_move)
    chosen_space = free_spaces[index]
    # print("Chosen space",chosen_space)
    board[chosen_space[0]][chosen_space[1]] = player_char

def is_victory_for(board, sign):
# The function analyzes the board's status in order to check if
# the player using 'O's or 'X's has won the game

    # check row victory
    for i in range(board_size):

        for j in range(board_size):
            break ## TODO fix this rest of this loop
            # if board[i][j]




# set up the board
# create a 2D list array
computer_char = "X"
player_char = "O"

# set up the board
board_size = 3
board = [[str((i + 1) + (j * 3)) for i in range(board_size)] for j in range(board_size)]  # 2D list comprehension

# computer moves first
draw_move(board)
display_board(board)

# do players move
enter_move(board)
display_board(board)

