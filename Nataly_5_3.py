##########################################################################
#Author: Nataly
#Date: 22.11.2021
#Task:
# to write a simple program which pretends to play tic-tac-toe 
# with the user. To make it all easier for you, we've decided
# to simplify the game. Here are our assumptions:
# • the computer (i.e., your program) should play the game using 'X's;
# • the user (e.g., you) should play the game using 'O's;
# • the first move belongs to the computer -it always puts its first
# 'X' in the middle of the board;
# • all the squares are numbered row by row starting with 1 the
# user inputs their move by entering the number of the square they 
# choose -the number must be valid, i.e., it must be an
# integer, it must be greater than 0 and less than 10, and it
# cannot point to a field which is already occupied;
# • the program checks if the game is over -there are four possible
# verdicts: the game should continue, or the game ends with a tie, 
# your win, or the computer's win;
# • the computer responds with its move and the check is repeated;
# • don't implement any form of artificial intelligence -a random
# field choice made by the computer is good enough for the game.
# Implement the following features:
# • the board should be stored as a three-element list, while each
# element is another three-element list (the inner lists represent
# rows) so that all of the squares may be accessed using the
# following syntax: board[row][column]
# • each of the inner list's elements can contain 'O', 'X', or a digit
# representing the square's number (such a square is considered free)
# • the board's appearance should be exactly the same as the one
# presented in the example.
# • implement the functions defined for you in the editor.
##########################################################################

# import randrange function from random package
from random import randrange

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


def victory_for(board, sgn):
    ''' Check if sgn von in the game or not
    Arguments: 
    board: two-dimentional array [3][3]
    sgn: 'X' or 'O'
    Retuns:
    - True if sgn won
    - False - otherwise      '''

    if board[0][0] == sgn and board[1][1] == sgn and board[2][2] == sgn:
            return True
    elif board[2][0] == sgn and board[1][1] == sgn and board[0][2] == sgn:
            return True
    else:
        for i in range(3):
            if board[i][0] == sgn and board[i][1] == sgn and board[i][2] == sgn:
                return True
            elif board[0][i] == sgn and board[1][i] == sgn and board[2][i] == sgn:
                return True
    return False


def check_step(board, step):
    ''' Check if step on free cell on not
    Arguments: 
    board: two-dimentional array [3][3]
    step: from 0 to 8
    Retuns:
    - None if no free cells left
    - True if step on free cell
    - False - otherwise      '''

    # set list of free cells on board
    free_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free_cells.append(i*3+j)

    if len(free_cells) == 0:
        return None     # no free cells left
    elif step in free_cells:
        return True     # step on free cell
    else:
        return False


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
        print("Step by computer:", end="")
    else:
        print("Step by user:", end="")

    # display current status of board
    display_board(board)

    return board    # retun updated board


# define board[3][3] and init it by cell number starting from 1
board = []
for i in range(3):
    row = [i*3+j+1 for j in range(3)]
    board.append(row)

# set first move from computer ('X') to center cell
board = move_on_board(board, 'X', 4)

# play game in loop
while True:
    move = input("Enter your move: ")   # ask user to do his move
    try:
        user_step = int(move) - 1
    except:
        print("Value not allowed, try again!")
        continue

    # check if user moves to busy cell
    if check_step(board, user_step) == False:
        print("Your move not in free cells. Try again!")
        continue

    board = move_on_board(board, 'O', user_step)

    # check if user won
    if victory_for(board, 'O'):
        print("You won! Congratulations!")
        break

    # generate computer's step
    comp_step = randrange(8)
    #print("randrange", comp_step)   # just to show result of random
    
    rc = check_step(board, comp_step)
    if rc == None: # check if no free cells left
        print("No free cells left. This is TIE!")
        break
    else:
        while rc != True:
            comp_step = randrange(8)
            #print("randrange", comp_step) # just to show result of random
            rc = check_step(board, comp_step)
    
    # step by computer
    board = move_on_board(board, 'X', comp_step)

    # check if computer won
    if victory_for(board, 'X'):
        print("Computer won! Sorry.")
        break