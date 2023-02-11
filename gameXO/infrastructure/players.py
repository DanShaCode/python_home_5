import os
import time
from infrastructure.print_board import *

def First_Player(board):
    os.system('cs||clear')
    print()
    index = 0
    for i in board:
        if index == 2 or index == 5:
            print(i)
            print()
            index += 1
        else:
            print(i, end = '  ')
            index += 1
    print()
    print()
    print("Ход Игрока_1")
    print()
    row = int(input("Введите номер строки: "))
    if row < 1 or row > 3:
        print()
        print("Ошбика ввода. Введите, пожалуйста, номер строки от 1 до 3.")
        time.sleep(2)
        return First_Player(board)
    col = int(input("Введите номер столбца: "))
    if col < 1 or col > 3:
        print()
        print("Ошбика ввода. Введите, пожалуйста, номер столбца от 1 до 3.")
        time.sleep(2)
        return First_Player(board)
    for i in board:
        if row == 1 and col == 1:
            if board[0] == '-':
                board[0] = 'X'
            elif board [0] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 1 and col == 2:
            if board[1] == '-':
                board[1] = 'X'
            elif board [1] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 1 and col == 3:
            if board[2] == '-':
                board[2] = 'X'
            elif board [2] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 2 and col == 1:
            if board[3] == '-':
                board[3] = 'X'
            elif board [3] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 2 and col == 2:
            if board[4] == '-':
                board[4] = 'X'
            elif board [4] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 2 and col == 3:
            if board[5] == '-':
                board[5] = 'X'
            elif board [5] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 3 and col == 1:
            if board[6] == '-':
                board[6] = 'X'
            elif board [6] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 3 and col == 2:
            if board[7] == '-':
                board[7] = 'X'
            elif board [7] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 3 and col == 3:
            if board[8] == '-':
                board[8] = 'X'
            elif board [8] == 'O':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board) 
    return board

def Second_PLayer(board):
    os.system('cs||clear')
    print()
    index = 0
    for i in board:
        if index == 2 or index == 5:
            print(i)
            print()
            index += 1
        else:
            print(i, end = '  ')
            index += 1
    print()
    print()
    print("Ход Игрока_2")
    print()
    row = int(input("Введите номер строки: "))
    if row < 1 or row > 3:
        print()
        print("Ошбика ввода. Введите, пожалуйста, номер строки от 1 до 3.")
        time.sleep(2)
        return Second_PLayer(board)
    col = int(input("Введите номер столбца: "))
    if col < 1 or col > 3:
        print()
        print("Ошбика ввода. Введите, пожалуйста, номер столбца от 1 до 3.")
        time.sleep(2)
        return Second_PLayer(board)
    for i in board:
        if row == 1 and col == 1:
            if board[0] == '-':
                board[0] = 'O'
            elif board [0] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 1 and col == 2:
            if board[1] == '-':
                board[1] = 'O'
            elif board [1] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 1 and col == 3:
            if board[2] == '-':
                board[2] = 'O'
            elif board [2] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 2 and col == 1:
            if board[3] == '-':
                board[3] = 'O'
            elif board [3] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 2 and col == 2:
            if board[4] == '-':
                board[4] = 'O'
            elif board [4] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 2 and col == 3:
            if board[5] == '-':
                board[5] = 'O'
            elif board [5] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 3 and col == 1:
            if board[6] == '-':
                board[6] = 'O'
            elif board [6] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 3 and col == 2:
            if board[7] == '-':
                board[7] = 'O'
            elif board [7] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board)
        if row == 3 and col == 3:
            if board[8] == '-':
                board[8] = 'O'
            elif board [8] == 'X':
                print("Эта клетка занята!")
                time.sleep(2)
                return First_Player(board) 
    return board

def First_Win_Check(board):
    for i in board:
        if  'X' == board[0] and 'X' == board[1] and 'X' == board[2]:
            return True
        elif  'X' == board[3] and 'X' == board[4] and 'X' == board[5]:
            return True
        elif  'X' == board[6] and 'X' == board[7] and 'X' == board[8]:
            return True
        elif  'X' == board[0] and 'X' == board[3] and 'X' == board[6]:
            return True
        elif  'X' == board[1] and 'X' == board[4] and 'X' == board[7]:
            return True
        elif  'X' == board[2] and 'X' == board[5] and 'X' == board[8]:
            return True
        elif  'X' == board[0] and 'X' == board[4] and 'X' == board[8]:
            return True
        elif  'X' == board[2] and 'X' == board[4] and 'X' == board[6]:
            return True
        else:
            return False

def Second_Win_Check(board):
    for i in board:
        if  'O' == board[0] and 'O' == board[1] and 'O' == board[2]:
            return True
        elif  'O' == board[3] and 'O' == board[4] and 'O' == board[5]:
            return True
        elif  'O' == board[6] and 'O' == board[7] and 'O' == board[8]:
            return True
        elif  'O' == board[0] and 'O' == board[3] and 'O' == board[6]:
            return True
        elif  'O' == board[1] and 'O' == board[4] and 'O' == board[7]:
            return True
        elif  'O' == board[2] and 'O' == board[5] and 'O' == board[8]:
            return True
        elif  'O' == board[0] and 'O' == board[4] and 'O' == board[8]:
            return True
        elif  'O' == board[2] and 'O' == board[4] and 'O' == board[6]:
            return True
        else:
            return False

def No_Win(board):
    flag = 0
    for i in board:
        if i == '-':
            flag += 1
        else:
            continue
    if flag > 0:
        return False
    else:
        return True
