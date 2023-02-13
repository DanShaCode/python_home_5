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

def player1 (candy_amount,first,second):
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
            if first == first_player_name:
                print("Ход", first, "Введите количество конфет: ", end = '')
                player_1 = int(input())
            if first == second_player_name:
                print("Ход", second, "Введите количество конфет: ", end = '')
                player_1 = int(input())  
        if player_1 < 0 or player_1 > 28:
            print()
            print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
            temp = candy_amount
            candy_amount = 0
            time.sleep(2)
            return player1(temp,first,second)
        else:
            candy_amount -= player_1
        if candy_amount <= 0:
            if first == first_player_name:
                return PlayerOneWin(candy_amount,first,second)
            if first == second_player_name:
                return PlayerTwoWin(candy_amount,first,second)
        elif candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            return player2(candy_amount,first,second)

def player2 (candy_amount,first,second):
    os.system('cls||clear')
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        if first == first_player_name:
            print("Ход", second, "Введите количество конфет: ", end = '')
            player_2 = int(input())
        if first == second_player_name:
            print("Ход", first, "Введите количество конфет: ", end = '')
            player_2 = int(input()) 
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
        return player1(candy_amount,first,second)
    elif candy_amount <= 0:
        if second == second_player_name:
            return PlayerTwoWin(candy_amount,first,second)
        if second == first_player_name:
            return PlayerOneWin(candy_amount,first,second)

def Game (candy_amount,first,second):
    os.system('cls||clear')
    if user_versus == 1:
        if candy_amount > 0:
            return player1(candy_amount)
        elif candy_amount - 1:
            return
    # Игра против Игрока
    elif user_versus == 2:
        if first == first_player_name:
            if candy_amount > 0:
                return player1(candy_amount,first,second)
        if first == second_player_name:
            if candy_amount > 0:
                return player2(candy_amount,first,second)

def PlayerOneWin(candy_amount, first,second):
    if candy_amount <= 0:
        time.sleep(2)
        print()
        print("Игра окончена.")
        print()
        print(first,"победил!")
        time.sleep(2)
        os.system('cls||clear')

def BotWin(candy_amount):
    if candy_amount <= 0:
        time.sleep(2)
        print()
        print("Игра окончена.")
        print()
        print("Бот победил!")
        time.sleep(2)
        os.system('cls||clear')

def PlayerTwoWin(candy_amount,first,second):
    if candy_amount <= 0:
        time.sleep(2)
        print()
        print("Игра окончена.")
        print()
        print(second, "победил!")
        time.sleep(2)
        os.system('cls||clear')

def GameType():
    print()
    print("Выберите режим игры.")
    print()
    print("1.Играть против ИИ")
    print("2.Играть против Игрока")
    print()

def Start(first,second):
    if user_versus == 1:
        os.system('cls||clear')
        print("Игра скоро начнется.")
        print()
        print("Загрузка ..... ")

        time.sleep(2)
        
        Game(221,first,second)
    elif user_versus == 2:
        os.system('cls||clear')
        print("Игра скоро начнется.")
        print()
        print("Загрузка ..... ")

        time.sleep(2)
        
        Game(221,first,second)

def Intro():
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
        os.system('cls||clear')
        f = open("game2021\Game_Rules.txt", "r")
        f_contents = f.read()
        print(f_contents)
        f.close()
        print()
        input("Нажмите Enter, как будете готовы начать игру")
        os.system('cls||clear')
    elif user_awnser == 'N' or user_awnser == 'n':
        os.system('cls||clear')

os.system('cs||clear')

Intro()

GameType()

user_versus = int(input("Введите номер режима сюда(1 или 2): "))

if user_versus == 2:
    print()
    first_player_name = input("Введите ваше Имя первого игрока: ")
    queue_1 = random.randint(1,2)
    print()
    second_player_name = input("Введите Имя второго игрока: ")
    queue_2 = random.randint(3,4)
    print()
    user_queue = input("Нажмите Enter, чтобы подбросить монетку ... ")
    print()
    if (queue_1 == 1 and queue_2 == 3) or (queue_1 == 1 and queue_2 == 4):
        os.system('cs||clear')
        print("Первым ходит", first_player_name)
        first = first_player_name
        print()
        print("Второй ход за", second_player_name)
        second = second_player_name
        time.sleep(3)
        Start(first,second)
    else:
        os.system('cs||clear')
        print("Первым ходит", second_player_name)
        first = second_player_name
        print()
        print("Второй ход за", first_player_name)
        second = first_player_name 
        time.sleep(3)
        Start(first,second)
if user_versus == 1:
    Start()