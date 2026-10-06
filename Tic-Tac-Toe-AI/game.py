def create_board():
    return [""] * 9


def display_board(board):
    print()
    print(f" {board[0] or ' '} | {board[1] or ' '} | {board[2] or ' '}")
    print("---+---+---")
    print(f" {board[3] or ' '} | {board[4] or ' '} | {board[5] or ' '}")
    print("---+---+---")
    print(f" {board[6] or ' '} | {board[7] or ' '} | {board[8] or ' '}")
    print()


def check_winner(board):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:

        if all(board[position] == "X" for position in combination):
            return "X"

        if all(board[position] == "O" for position in combination):
            return "O"

    return None


def is_board_full(board):
    return all(cell != "" for cell in board)


def get_available_moves(board):
    return [index for index, cell in enumerate(board) if cell == ""]


def make_move(board, position, player):
    if position < 0 or position > 8:
        return False

    if board[position] != "":
        return False

    board[position] = player
    return True