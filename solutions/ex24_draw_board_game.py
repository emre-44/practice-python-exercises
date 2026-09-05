def write_a_board():
    size = int(input("Input game board size: "))
    board = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(' ')
        board.append(row)

    return board

def print_a_board(board):
    size = len(board)

    for i in range(size):
        row_str = ""
        for j in range(size):
            row_str += f" {board[i][j]} "
            if j < size - 1:
                row_str += "|"
        print(row_str)

        if i < size - 1:
            print("---" + "+---" * (size - 1))

# Test Stage
board = write_a_board()
print_a_board(board)