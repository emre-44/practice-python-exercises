def tic_tac_toe_draw():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    turn = 0
    total_moves = 0
    while total_moves < 9:
        for row in board:
            print(row)

        player = "X" if turn == 0 else "O"

        user_input = input(f"{player} player, input your move (row column): ").split()
        if not user_input or len(user_input) != 2:
            print("Input 2 value!")
            continue

        row = int(user_input[0])
        col = int(user_input[1])

        if row not in [0,1,2] or col not in [0,1,2]:
            print("Input 0,1,2 values!")
            continue
        if board[row][col] != 0:
            print("This cell is full! Choose another cell")
            continue
        board[row][col] = player
        total_moves += 1

        turn = 1 - turn

    print("Game Over!")
    for row in board:
        print(row)

    return board

print(tic_tac_toe_draw())
