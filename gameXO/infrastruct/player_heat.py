import random
from infrastruct.intro import *
from infrastruct.print_board import *
from infrastruct.players import *

def Player_Heat(player_one_name, player_two_name):
    first = random.randint(1,2)
    second = random.randint(3,4)
    if first == 1 and second == 3 or first == 1 and second == 4:
        player_start_first = player_one_name
        return player_start_first
    else:
        player_start_first = player_two_name
        return player_start_first