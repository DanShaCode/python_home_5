from infrastruct.intro import *
from infrastruct.print_board import *
from infrastruct.game_round import *
from infrastruct.players import *
from infrastruct.player_heat import*

start_board = Introduction()
player_one_name = input("Введите Имя первого игрока: ")
player_two_name = input("Введите Имя второго игрока: ")
player_start_first = Player_Heat(player_one_name, player_two_name)
Game_Round(start_board,player_start_first,player_one_name,player_two_name)