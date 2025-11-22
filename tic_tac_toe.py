def print_board(board):
    """Print the current board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    """Return True if player ('X' or 'O') has won."""
    winning_positions = [
        (0, 1, 2),  # rows
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # columns
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6),
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    """Return True if the board is full (no numbers left)."""
    for cell in board:
        if cell != "X" and cell != "O":
            return False
    return True

def get_valid_move(board):
    """Ask the current player to choose a valid empty position (1-9)."""
    while True:
        move = input("Choose a position (1-9): ").strip()
        if not move.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        pos = int(move)
        if pos < 1 or pos > 9:
            print("Number must be between 1 and 9.")
            continue

        if board[pos - 1] in ["X", "O"]:
            print("That position is already taken. Try again.")
            continue

        return pos - 1  # index 0-8


def play_game():
    """Main game loop for Tic Tac Toe."""
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Player X and Player O take turns.")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        move_index = get_valid_move(board)
        board[move_index] = current_player

        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print("It's a draw (no more moves).")
            break

        # switch player
        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing Tic Tac Toe. Goodbye!")
            break


if __name__ == "__main__":
    main()