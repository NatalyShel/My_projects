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