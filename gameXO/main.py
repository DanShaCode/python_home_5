from infrastruct.intro import *
from infrastruct.print_board import *
from infrastruct.game_round import *
from infrastruct.players import *
from infrastruct.player_heat import*

start_board = Introduction()
print()
print()
player_one_name = input("       -=XOXOXO=- Введите Имя первого игрока: ")
print()
player_two_name = input("       -=XOXOXO=- Введите Имя второго игрока: ")
player_start_first = Player_Heat(player_one_name, player_two_name)
print()
user_heat = input("        Нажмите Enter, чтобы подбросить монетку ... 0 ")
print()
print("        Первый ход за", player_start_first, '!')
print()
time.sleep(2)
Game_Round(start_board,player_start_first,player_one_name,player_two_name)