def game():
    tic_tac_toe = [[0, 0, 0], [0 ,0 ,0], [0, 0, 0]]
    print("Welcome to the Tic Tac Toe Game")
    draw(tic_tac_toe)
    print("Based on the table, choose a number and set your position.")
    while game:
        player_one = int(input("Player 1 (X) Turn: "))
        count = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if player_one == count:
                    tic_tac_toe[i][j] = 1
                count += 1
        if checkGrid(tic_tac_toe) == 1:
            draw(tic_tac_toe)
            print("Player One Wins!")
            break
        elif checkGrid(tic_tac_toe) == 2:
            draw(tic_tac_toe)
            print("Player Two Wins!")
            break
        draw(tic_tac_toe)
        player_two = int(input("Player 2 (O) Turn: "))
        count = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if player_two == count:
                    tic_tac_toe[i][j] = 2
                count += 1
        checkGrid(tic_tac_toe)
        draw(tic_tac_toe)


def draw(tic_tac_toe):

    for i in range(0, 3):
        print(" ---" * 3 + "\n", end ='')
        print("|", end='')
        for j in range(0, 3):
            if tic_tac_toe[i][j] == 0:
                print("   |", end='')
            elif tic_tac_toe[i][j] == 1:
                print(" X |", end='')
            elif tic_tac_toe[i][j] == 2:
                print(" O |", end='')
        if i == 0:
            print(" [1, 2, 3]")
        elif i == 1:
            print(" [4, 5, 6]")
        elif i == 2:
            print(" [7, 8, 9]")
    print(" ---" * 3)


def checkGrid(grid):
    # rows
    for x in range(0, 3):
        row = set([grid[x][0], grid[x][1], grid[x][2]])
        if len(row) == 1 and grid[x][0] != 0:
            return grid[x][0]

    # columns
    for x in range(0, 3):
        column = set([grid[0][x], grid[1][x], grid[2][x]])
        if len(column) == 1 and grid[0][x] != 0:
            return grid[0][x]

    # diagonals
    diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
    diag2 = set([grid[0][2], grid[1][1], grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]
    return 0


tic_tac_toe = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

if __name__ == "__main__":
  game()
