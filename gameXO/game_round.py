from intro import *
from print_board import *
import os

def Game_Round(start_board):
    os.system('cs||clear')
    Print(start_board)
    first_board = First_Player(start_board)
    os.system('cs||clear')
    Print(first_board)
    second_board = Second_Player(first_board)
    os.system('cs||clear')
    Print(second_board)
    Game_Round(second_board)