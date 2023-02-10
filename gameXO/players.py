
def First_Player(board):
    row = int(input("Введите номер строки: "))
    col = int(input("Введите номер колонки: "))
    for i in board:
        if row == 1 and col == 1:
            board[0] = 'X'
        if row == 1 and col == 2:
            board[1] = 'X'
        if row == 1 and col == 3:
            board[2] = 'X'
        if row == 2 and col == 1:
            board[3] = 'X'
        if row == 2 and col == 2:
            board[4] = 'X'
        if row == 2 and col == 3:
            board[5] = 'X'
        if row == 3 and col == 1:
            board[6] = 'X'
        if row == 3 and col == 2:
            board[7] = 'X'
        if row == 3 and col == 3:
            board[8] = 'X'    
    return board

def Second_Player(board):
    row = int(input("Введите номер строки: "))
    col = int(input("Введите номер колонки: "))
    for i in board:
        if row == 1 and col == 1:
            board[0] = 'O'
        if row == 1 and col == 2:
            board[1] = 'O'
        if row == 1 and col == 3:
            board[2] = 'O'
        if row == 2 and col == 1:
            board[3] = 'O'
        if row == 2 and col == 2:
            board[4] = 'O'
        if row == 2 and col == 3:
            board[5] = 'O'
        if row == 3 and col == 1:
            board[6] = 'O'
        if row == 3 and col == 2:
            board[7] = 'O'
        if row == 3 and col == 3:
            board[8] = 'O'    
    return board