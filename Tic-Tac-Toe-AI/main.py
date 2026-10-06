from game import (
    create_board,
    display_board,
    check_winner,
    is_board_full,
    make_move
)

from minimax import get_best_move


def get_human_move(board):

    while True:

        try:
            position = int(input("Choose a position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Please choose a number from 1 to 9.")
                continue

            if board[position] != "":
                print("That position is already occupied.")
                continue

            return position

        except ValueError:
            print("Please enter a valid number.")


def play_game():

    board = create_board()

    print("\n==============================")
    print("      TIC-TAC-TOE AI")
    print("==============================")

    print("\nYou are X.")
    print("The AI is O.")

    print("""
Positions:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

    current_player = "X"

    while True:

        display_board(board)

        if current_player == "X":

            position = get_human_move(board)
            make_move(board, position, "X")

        else:

            print("AI is thinking...")

            position = get_best_move(board)
            make_move(board, position, "O")

        winner = check_winner(board)

        if winner is not None:

            display_board(board)

            if winner == "X":
                print("Congratulations! You won!")

            else:
                print("The AI won!")

            break

        if is_board_full(board):

            display_board(board)
            print("It's a draw!")

            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():

    while True:

        play_game()

        choice = input("\nPlay again? (y/n): ").strip().lower()

        if choice != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()