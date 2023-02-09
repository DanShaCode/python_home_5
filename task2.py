# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import os
import time
import random

def Bot_Player(candy_amount):
    os.system('cls||clear')
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        print("Ход Бота.")
        bot_player = random.randint(1, 28)
        candy_amount -= bot_player
    if candy_amount <= 0:
        Game(candy_amount - 3)
    elif candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        player1(candy_amount)

def player1 (candy_amount):
    os.system('cls||clear')
    if players == 1:
        if candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            player_1 = int(input("Ход Игрока_1. Введите количество конфет: "))
        if player_1 < 1 or player_1 > 500:
            print()
            print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
            temp = candy_amount
            candy_amount = 0
            time.sleep(2)
            player1(temp)
        else:
            candy_amount -= player_1
        if candy_amount <= 0:
            Game(candy_amount - 1)
        elif candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            Bot_Player(candy_amount)       
    if players == 2:
        if candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            player_1 = int(input("Ход Игрока_1. Введите количество конфет: "))
        if player_1 < 1 or player_1 > 500:
            print()
            print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
            temp = candy_amount
            candy_amount = 0
            time.sleep(2)
            player1(temp)
        else:
            candy_amount -= player_1
        if candy_amount <= 0:
            Game(candy_amount - 1)
        elif candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            player2(candy_amount)

def player2 (candy_amount):
    os.system('cls||clear')
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        player_2 = int(input("Ход Игрока_2. Введите количество конфет: "))
    if player_2 < 1 or player_2 > 500:
        print()
        print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
        temp = candy_amount
        candy_amount = 0
        time.sleep(2)
        player2(temp)
    else:
        candy_amount -= player_2
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        Game(candy_amount)
    elif candy_amount <= 0:
        Game(candy_amount - 2)

def Game (candy_amount):
    os.system('cls||clear')
    if players == 1:
        if candy_amount > 0:
            player1(candy_amount)
        elif candy_amount <= 0 and candy_amount - 1:
            print()
            print("Игра окончена!")
            print()
            print("Игрок победил!")
            time.sleep(2)
            os.system('cls||clear')
        elif candy_amount <= 0 and candy_amount - 3:
            print()
            print("Игра окончена!")
            print()
            print("Бот победил!")
            time.sleep(2)
            os.system('cls||clear')
    # Игра против Игрока
    elif players == 2:
        if candy_amount > 0:
            player1(candy_amount)
        elif candy_amount <= 0 and candy_amount - 1:
            print()
            print("Игра окончена!")
            print()
            print("Игрок_1 победил!")
            time.sleep(2)
            os.system('cls||clear')
        elif candy_amount <= 0 and candy_amount - 2:
            print()
            print("Игра окончена!")
            print()
            print("Игрок_2 победил!")
            time.sleep(2)
            os.system('cls||clear')
        elif candy_amount <= 0 and candy_amount - 3:
            print()
            print("Игра окончена!")
            print()
            print("Бот победил!")
            time.sleep(2)
            os.system('cls||clear')

print()
print("Игра началась!")
print()

time.sleep(2)

players = 1

Game(2021)