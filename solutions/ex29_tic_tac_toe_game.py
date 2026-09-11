def write_a_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(0)   
        board.append(row)
    return board

def print_a_board(board):
    size = len(board)
    for i in range(size):
        row_str = ""
        for j in range(size):

            cell = board[i][j] if board[i][j] != 0 else ' '
            row_str += f" {cell} "
            if j < size - 1:
                row_str += "|"
        print(row_str)
        if i < size - 1:
            print("---" + "+---" * (size - 1))
    print()

def check_tic_tac_toe(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return None

def tic_tac_toe_draw():
    board = write_a_board()
    turn = 0
    total_moves = 0

    while total_moves < 9:
        print_a_board(board)   
        player = "X" if turn == 0 else "O"

        user_input = input(f"{player} player, input your move (row column): ").split()
        if not user_input or len(user_input) != 2:
            print("Input 2 value!")
            continue

        try:
            row = int(user_input[0])
            col = int(user_input[1])
        except ValueError:
            print("Please enter numbers only!")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Input 0, 1, or 2 values!")
            continue
        if board[row][col] != 0:
            print("This cell is full! Choose another cell")
            continue

        board[row][col] = player
        total_moves += 1

        winner = check_tic_tac_toe(board)
        if winner:
            print_a_board(board)
            print(f"Congratulations! Winner is {winner} 🎉")
            return winner

        turn = 1 - turn

    print_a_board(board)
    print("It's a draw! Game Over.")
    return None

def main():
    scores = {"X": 0, "O": 0, "Draw": 0}
    while True:
        winner = tic_tac_toe_draw()
        if winner:
            scores[winner] += 1
        else:
            scores["Draw"] += 1

        print(f"\nScore: X = {scores['X']} | O = {scores['O']} | Draw = {scores['Draw']}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
