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
        print()
        bot_player = random.randint(0, 28)
        print("Бот взял ", bot_player, "конфет." )
        time.sleep(2)
        candy_amount -= bot_player
    if candy_amount <= 0:
        return BotWin(candy_amount)
    elif candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        return player1(candy_amount)

def player1 (candy_amount):
    # Игра против Бота
    os.system('cls||clear')
    if user_versus == 1:
        if candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            player_1 = int(input("Ход Игрока_1. Введите количество конфет: "))
        if player_1 < 0 or player_1 > 28:
            print()
            print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
            temp = candy_amount
            candy_amount = 0
            time.sleep(2)
            return player1(temp)
        else:
            candy_amount -= player_1
        if candy_amount <= 0:
            return PlayerOneWin(candy_amount)
        elif candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            return Bot_Player(candy_amount)
    # Игра против Игрока       
    if user_versus == 2:
        if candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            player_1 = int(input("Ход Игрока_1. Введите количество конфет: "))
        if player_1 < 0 or player_1 > 28:
            print()
            print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
            temp = candy_amount
            candy_amount = 0
            time.sleep(2)
            return player1(temp)
        else:
            candy_amount -= player_1
        if candy_amount <= 0:
            return Game(candy_amount - 1)
        elif candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            return player2(candy_amount)

def player2 (candy_amount):
    os.system('cls||clear')
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        player_2 = int(input("Ход Игрока_2. Введите количество конфет: "))
    if player_2 < 0 or player_2 > 28:
        print()
        print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
        temp = candy_amount
        candy_amount = 0
        time.sleep(2)
        return player2(temp)
    else:
        candy_amount -= player_2
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        return Game(candy_amount)
    elif candy_amount <= 0:
        return PlayerTwoWin(candy_amount)

def Game (candy_amount):
    os.system('cls||clear')
    if user_versus == 1:
        if candy_amount > 0:
            return player1(candy_amount)
        elif candy_amount - 1:
            return
    # Игра против Игрока
    elif user_versus == 2:
        if candy_amount > 0:
            return player1(candy_amount)
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

def PlayerOneWin(candy_amount):
    if candy_amount <= 0:
        time.sleep(2)
        print()
        print("Игра окончена.")
        print()
        print("Игрок_1 победил!")

def BotWin(candy_amount):
    if candy_amount <= 0:
        time.sleep(2)
        print()
        print("Игра окончена.")
        print()
        print("Бот победил!")

def PlayerTwoWin(candy_amount):
    if candy_amount <= 0:
        time.sleep(2)
        print()
        print("Игра окончена.")
        print()
        print("Игрок_2 победил!")

def Start():
    if user_versus == 1:
        os.system('cls||clear')
        print("Игра началась!")
        print()

        time.sleep(2)
        
        Game(221)
    elif user_versus == 2:
        os.system('cls||clear')
        print("Игра началась!")
        print()

        time.sleep(2)
        
        Game(221)

print()
print("Добро пожаловать!")
print()
print("Вы запустили интерактивную игру 2021!")
print()
print("Хотите прочитать правила?")
print()
user_awnser = str(input("Введите Y/N: "))
print()
if user_awnser == 'Y' or user_awnser == 'y':
    f = open("GameRules.txt", "r")
    f_contents = f.read()
    print(f_contents)
    f.close()
    print()
    close = input("Нажмите Enter, как будете готовы начать игру")
    os.system('cls||clear')
    print()
    print("Выберите режим игры.")
    print()
    print("1.Играть против ИИ")
    print("2.Играть против Игрока")
    user_versus = int(input("Введите номер режима сюда(1 или 2): "))
    Start()