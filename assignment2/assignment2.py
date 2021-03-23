board_size = 0
board = []  # stores the initial board state.
moves = []  # keeps track of the moves that was made, keeps things cleaner.


def is_invalid_move(player, index):
    if index < 0 or index >= board_size ** 2:
        return "Please enter a valid number"
    if [player, index] in moves:
        return "You have already made this move."
    if ['Player 1' if player == "Player 2" else 'Player 2', index] in moves:
        return "Other player has already made this move."


def process_input(player):
    move = int(input("{} turn --> ".format(player)))
    result = is_invalid_move(player, move)
    if result is None:
        moves.append([player, move])
        board[move // board_size][move % board_size] = 'X' if player == "Player 1" else 'O'  # might seem odd, but works
    else:
        print(result)
    render_board()
    winner = get_winner()
    if winner is not None:
        print("Winner: {}".format(winner))
        exit()


def initialize_board():
    global board_size, board
    board_size = int(input("Please enter the size of the board: "))
    board = [[(board_size * j + i) for i in range(board_size)] for j in range(board_size)]
    render_board()


def render_board():
    width = 5  # fixed width for numbers, so they align up correctly.
    for row in board:
        for i in row:
            print(str(i).center(width), end='')
        print()


def check_list_for_winner(it):
    return 'X' if it.count('X') == board_size else 'O' if it.count('O') == board_size else None


def get_winner():  # should return 'X' or 'O' or 'Draw!' or None
    winner = None
    for row in board:  # check rows for winner
        winner = check_list_for_winner(row) if winner is None else winner

    for column in zip(*board):  # translates our matrix, so now columns are rows, ez to iterate
        winner = check_list_for_winner(column) if winner is None else winner

    diagonals = [[board[i][i] for i in range(board_size)], [board[i][-i - 1] for i in range(board_size)]]
    for diag in diagonals:
        winner = check_list_for_winner(diag) if winner is None else winner

    winner = "Draw!" if len(moves) == board_size**2 and winner is None else winner
    return winner


initialize_board()
while True:  # main game loop
    process_input("Player 1")
    process_input("Player 2")
