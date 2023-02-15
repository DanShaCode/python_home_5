import os

def Introduction():
    os.system('cs||clear')
    print()
    print("                  Добро пожаловать!                ")
    print()
    print("XOOXOXOXO-----------------------------------OXOOXOXO")
    print("OXOXOXOXO Вы запустили игру Крестики-Нолики XOXOXOXO")
    print("XOOXOXOXO-----------------------------------XOXOXOXO")
    print()
    user_enter = input(("        нажмите Enter для начала игры .... "))
    print()
    start_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    os.system('cs||clear')
    return start_board