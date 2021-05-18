board = [' '] * 10


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def checkSpace(pos):
    global board
    if board[pos] == ' ':
        board[pos] = 'X'
        return True
    else:
        print("This space is occupied!")
        return False


def userSpace():
    pos = input("Select the position you want you place your 'X' (1-9) ")
    while True:
        try:
            pos = int(pos)
            while pos > 9 or pos < 1:
                pos = input(
                    "Select the position you want you place your 'X' (1-9) ")
            break
        except ValueError:
            pos = input(
                "Select the position you want you place your 'X' (1-9) ")
    return pos


if __name__ == "__main__":
    print("Welcome to Boris' game of Tic Tac Toe!")
    while True:
        drawBoard(board)
        pos = userSpace()
        check = checkSpace(pos)
        while check == False:
            pos = userSpace()
            check = checkSpace(pos)
