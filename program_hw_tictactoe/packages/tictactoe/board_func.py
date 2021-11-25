def display_board(board):
    ''' Draw board for game TIC TAC TOE
        1 2 3
        4 5 6
        7 8 9
    Argument: two-dimentional array [3][3] -> board[row][column]  '''

    print()
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       " * 3, "|", sep="")
        for j in range(3):
            print("|   " + str(board[i][j]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
    print()


def move_on_board(board, sgn, step):
    ''' Set move on board
    Arguments: 
    - board: two-dimentional array [3][3]
    - sgn: 'X' or 'O'
    - step: from 0 to 8
    Retuns updated board   '''

    line = step // 3    # calculate line of user step
    col = step % 3      # calculate column of user step

    # set move on board
    board[line][col] = sgn

    if sgn == 'X':
        print("Step by computer:", step+1, end="")
    else:
        print("Step by user:", end="")

    # display current status of board
    display_board(board)

    return board    # retun updated board