import os

def Introduction():
    os.system('cs||clear')
    print()
    print("Это игра в крестики - нолики")
    print()
    user_enter = input(("нажмите Enter для начала игры .... "))
    print()
    start_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    os.system('cs||clear')
    return start_board