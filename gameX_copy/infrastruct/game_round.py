from infrastruct.intro import *
from infrastruct.print_board import *
from infrastruct.players import *
import os

def Game_Round(start_board,player_start_first,player_one_name,player_two_name):
    os.system('cs||clear')
    if player_start_first == player_one_name:
        Board_Print(start_board)
        first_board = First_Player(start_board,player_one_name)
        first_check = First_Win_Check(first_board)
        no_win_check_first = No_Win(first_board)
        if first_check == True:
            Board_Print(first_board)
            print()
            print(player_one_name,"победил!")
            time.sleep(2)
            os.system('cs||clear')
        if no_win_check_first == True:
            Board_Print(first_board)
            print()
            print("Ничья!")
            time.sleep(2)
            os.system('cs||clear')
        elif no_win_check_first == False and first_check == False:
            os.system('cs||clear')
            Board_Print(first_board)
            second_board = Second_PLayer(first_board,player_two_name)
            second_check = Second_Win_Check(second_board)
            no_win_check_second = No_Win(second_board)
            if second_check == True:
                Board_Print(second_board)
                print()
                print(player_two_name,"победил!")
                time.sleep(2)
                os.system('cs||clear')
            if no_win_check_second == True:
                Board_Print(first_board)
                print()
                print("Ничья!")
                time.sleep(2)
                os.system('cs||clear')    
            elif second_check == False and no_win_check_second == False:
                Game_Round(second_board,player_start_first,player_one_name,player_two_name)
    # Второй игрок
    os.system('cs||clear')
    if player_start_first == player_two_name:
        Board_Print(start_board)
        second_board = Second_PLayer(start_board,player_two_name)
        second_check = Second_Win_Check(second_board)
        no_win_check_second = No_Win(second_board)
        if second_check == True:
            Board_Print(second_board)
            print()
            print(player_two_name,"победил!")
            time.sleep(2)
            os.system('cs||clear')
        if no_win_check_second == True:
            Board_Print(second_board)
            print()
            print("Ничья!")
            time.sleep(2)
            os.system('cs||clear')
        elif no_win_check_second == False and second_check == False:
            os.system('cs||clear')
            Board_Print(second_board)
            # далее менять все наоборот
            first_board = First_Player(second_board,player_one_name)
            first_check = First_Win_Check(first_board)
            no_win_check_first = No_Win(first_board)
            if first_check == True:
                Board_Print(first_board)
                print()
                print(player_one_name,"победил!")
                time.sleep(2)
                os.system('cs||clear')
            if no_win_check_first == True:
                Board_Print(first_board)
                print()
                print("Ничья!")
                time.sleep(2)
                os.system('cs||clear')    
            elif first_check == False and no_win_check_first == False:
                Game_Round(first_board,player_start_first,player_one_name,player_two_name)