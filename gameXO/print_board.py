from players import *

def Print(board):
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


    

    