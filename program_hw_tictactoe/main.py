##########################################################################
#Author: Nataly
#Date: 25.11.2021
#Task: (to use package structure)
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

from sys import path
#path.append("c:\\Users\\tillo\\git_proj\\My_projects\\program_hw_tictactoe\\packages")
path.append("..\\packages")

# import my functions
from packages.tictactoe import board_func, check_func

# import randrange function from random package
from random import randrange


# define board[3][3] and init it by cell number starting from 1
board = []
for i in range(3):
    row = [i*3+j+1 for j in range(3)]
    board.append(row)

# set first move from computer ('X') to center cell
board = board_func.move_on_board(board, 'X', 4)

# play game in loop
while True:
    move = input("Enter your move: ")   # ask user to do his move
    try:
        user_step = int(move) - 1
    except:
        print("Value not allowed, try again!")
        continue

    # check if user moves to busy cell
    if check_func.check_step(board, user_step) == False:
        print("Your move not in free cells. Try again!")
        continue

    board = board_func.move_on_board(board, 'O', user_step)

    # check if user won
    if check_func.victory_for(board, 'O'):
        print("You won! Congratulations!")
        break

    # generate computer's step
    comp_step = randrange(8)
    #print("randrange", comp_step)   # just to show result of random
    
    rc = check_func.check_step(board, comp_step)
    
    if rc == None: # check if no free cells left
        print("No free cells left. This is TIE!")
        break
    else:
        while rc != True:
            comp_step = randrange(8)
            #print("randrange", comp_step) # just to show result of random
            rc = check_func.check_step(board, comp_step)
    
    # step by computer
    board = board_func.move_on_board(board, 'X', comp_step)

    # check if computer won
    if check_func.victory_for(board, 'X'):
        print("Computer won! Sorry.")
        break
