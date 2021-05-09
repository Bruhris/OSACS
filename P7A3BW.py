board = []

for x in range(5):
    board.append(["[       ]"] * 5)


def print_board(board):
    # Function to add the elements of list with " "
    for row in board:
        print("".join(row))


print_board(board)

row = int(input())
column = int(input())

if row == 4 and column == 1:
    board[row][column] = "[ Pizza ]"
    print(board[row][column])
print_board(board)
