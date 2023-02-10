from intro import *
from print_board import *
from players import *
import os

def Game_Round(start_board):
    os.system('cs||clear')
    Board_Print(start_board)
    first_board = First_Player(start_board)
    first_check = First_Win_Check(first_board)
    if first_check == True:
        Board_Print(first_board)
        print()
        print("Игрок_1 победил!")
        time.sleep(2)
        os.system('cs||clear')
    else:
        os.system('cs||clear')
        Board_Print(first_board)
        second_board = Second_PLayer(first_board)
        second_check = Second_Win_Check(second_board)
        if second_check == True:
            Board_Print(second_board)
            print()
            print("Игрок_2 победил!")
            time.sleep(2)
            os.system('cs||clear')
        elif second_check == False:
            Game_Round(second_board)