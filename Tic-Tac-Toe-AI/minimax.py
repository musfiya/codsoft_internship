from game import check_winner, is_board_full, get_available_moves


def minimax(board, depth, is_maximizing):

    winner = check_winner(board)

    if winner == "O":
        return 1
    0 - depth

    if winner == "X":
        return depth - 10

    if is_board_full(board):
        return 0

    if is_maximizing:

        best_score = float("-inf")

        for move in get_available_moves(board):

            board[move] = "O"

            score = minimax(board, depth + 1, False)

            board[move] = ""

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = float("inf")

        for move in get_available_moves(board):

            board[move] = "X"

            score = minimax(board, depth + 1, True)

            board[move] = ""

            best_score = min(best_score, score)

        return best_score


def get_best_move(board):

    best_score = float("-inf")
    best_move = None

    for move in get_available_moves(board):

        board[move] = "O"

        score = minimax(board, 0, False)

        board[move] = ""

        if score > best_score:
            best_score = score
            best_move = move

    return best_move