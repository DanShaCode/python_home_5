# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import os
import time

def player1 (candy_amount):


def Game (candy_amount):
    os.system('cls||clear')
    print("Начало нового раунда!")
    flag = 0
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        flag += 1
        player_1 = int(input("Ход Игрока_1. Введите количество конфет: "))
    if player_1 < 1 or player_1 > 500:
        print()
        print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
        time.sleep(2)
    else:
        candy_amount -= player_1
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
    if candy_amount > 0:
        os.system('cls||clear')
        print("Начало нового раунда!")
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        flag -= 1
        player_2 = int(input("Ход Игрока_2. Введите количество конфет: "))
    if player_2 < 1 or player_2 > 500:
        print()
        print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
        time.sleep(2)
        error2 += 1
    elif error2 == 0:
        candy_amount -= player_2
    if candy_amount <= 0:
        if flag == 0:
            print()
            print("Конец игры. Игрок_2 выйграл!")
        else:
            print("Конец игры. Игрок_1 выйграл!")
    elif candy_amount > 0:
        Game(candy_amount)

Game(2021)

    


