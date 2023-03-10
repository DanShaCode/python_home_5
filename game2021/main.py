import os
import time
import random

def Bot_Player(candy_amount,first,second):
    os.system('cls||clear')
    if candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        print("Ход Бота.")
        print()
        # Органичение на взятие конфет
        if candy_amount > 28:
            bot_player = random.randint(0, 28)
        elif candy_amount <= 28:
            bot_player = candy_amount
        print("Бот взял ", bot_player, "конфет." )
        time.sleep(2)
        candy_amount -= bot_player
    if candy_amount <= 0:
            if second == bot_name:
                return BotWin(candy_amount)
            if second == player_name:
                return BotWin(candy_amount)
    elif candy_amount > 0:
        print()
        print("Количество конфет на столе: ", candy_amount)
        print()
        return player1(candy_amount,first,second)

def player1 (candy_amount,first,second):
    # Игра против Бота ===============================================
    os.system('cls||clear')
    if user_versus == 1:
        if candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            if first == player_name:
                print("Ход", first, "Введите количество конфет: ", end = '')
                player_1 = int(input())
            if second == player_name:
                print("Ход", second, "Введите количество конфет: ", end = '')
                player_1 = int(input())
        # Ограничение на взятие конфет если их <= 28
        if candy_amount <= 28:
            if player_1 > candy_amount:
                print()
                print("Вы не можете взять конфет больше, чем лежит на столе!")
                temp = candy_amount
                candy_amount = 0
                time.sleep(2)
                return player1(temp,first,second)  
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
            if first == player_name:
                return PlayerOneWin(candy_amount,first,second)
            if first == bot_name:
                return PlayerTwoWin(candy_amount,first,second)
        elif candy_amount > 0:
            print()
            print("Количество конфет на столе: ", candy_amount)
            print()
            return Bot_Player(candy_amount,first,second)
    # Игра против Игрока  ===========================================    
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
        # Ограничение на взятие конфет если их <= 28
        if candy_amount <= 28:
            if player_1 > candy_amount:
                print()
                print("Вы не можете взять конфет больше, чем лежит на столе!")
                temp = candy_amount
                candy_amount = 0
                time.sleep(2)
                return player1(temp,first,second)  
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
        # Ограничение на взятие конфет если их <= 28
        if candy_amount <= 28:
            if player_2 > candy_amount:
                print()
                print("Вы не можете взять конфет больше, чем лежит на столе!")
                temp = candy_amount
                candy_amount = 0
                time.sleep(2)
                return player2(temp,first,second)  
    if player_2 < 0 or player_2 > 28:
        print()
        print("Количество конфет, которые вы берете не может быть меньше 0 или больше 28!")
        temp = candy_amount
        candy_amount = 0
        time.sleep(2)
        return player2(temp,first,second)
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
    # Игра протв Бота
    if user_versus == 1:
        if first == player_name:
            if candy_amount > 0:
                return player1(candy_amount,first,second)
        if first == bot_name:
            if candy_amount > 0:
                return Bot_Player(candy_amount,first,second)
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
        print(first,"победил(а)!")
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
        print(second, "победил(а)!")
        time.sleep(2)
        os.system('cls||clear')

def GameType():
    print()
    print(" !@#$%^&* --^ ВЫБЕРИТЕ РЕЖИМ ИГРЫ ^-- *&^%$#@!")
    print()
    print("             1.Играть против ИИ")
    print()
    print("           2.Играть против Игрока")
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
    print("             -^-^- Добро пожаловать! -^-^-")
    print()
    print("     >>> Вы запустили интерактивную игру 2021! <<<")
    print()
    print("             Хотите прочитать правила? O_0")
    print()
    user_awnser = str(input("                    Введите Y/N: "))
    print()
    if user_awnser == 'Y' or user_awnser == 'y':
        os.system('cls||clear')
        f = open("game2021\Game_Rules.txt", "r")
        f_contents = f.read()
        print(f_contents)
        f.close()
        print()
        input("Нажмите Enter, как будете готовы начать игру ... ")
        os.system('cls||clear')
    elif user_awnser == 'N' or user_awnser == 'n':
        os.system('cls||clear')
    else:
        os.system('cls||clear')

os.system('cs||clear')

Intro()

GameType()

user_versus = int(input("    Введите номер режима сюда (1 или 2): "))

if user_versus == 2:
    os.system('cs||clear')
    print()
    print()
    first_player_name = input("        0_o .. Введите ваше Имя первого игрока: ")
    queue_1 = random.randint(1,2)
    print()
    second_player_name = input("        o_0 .. Введите Имя второго игрока: ")
    queue_2 = random.randint(3,4)
    print()
    user_queue = input("        Нажмите Enter, чтобы подбросить монетку ... 0")
    print()
    if (queue_1 == 1 and queue_2 == 3) or (queue_1 == 1 and queue_2 == 4):
        os.system('cs||clear')
        print("Судьба распорядилась следующим псевдослучайным образом!")
        print()
        print("(I_o) Первым ходит", first_player_name)
        first = first_player_name
        print()
        print("(-_p) Второй ход за", second_player_name)
        second = second_player_name
        print()
        print('Удачной игры!')
        time.sleep(4)
        Start(first,second)
    else:
        os.system('cs||clear')
        print("Судьба распорядилась следующим псевдослучайным образом!")
        print()
        print("(I_o) Первым ходит", second_player_name)
        first = second_player_name
        print()
        print("(-_p) Второй ход за", first_player_name)
        second = first_player_name 
        print()
        print('Удачной игры!')
        time.sleep(4)
        Start(first,second)
if user_versus == 1:
    os.system('cs||clear')
    print()
    player_name = input("(0_0) Введите ваше Имя: ")
    queue_1 = random.randint(1,2)
    print()
    print("Очень приятно", player_name, "! Я бот и меня зовут - Бот. Давай сыграем в игру!")
    bot_name = 'Бот' 
    queue_2 = random.randint(3,4)
    print()
    user_queue = input("Нажмите Enter, чтобы подбросить монетку ... 0")
    os.system('cs||clear')
    print()
    print("Хеееей. Погоди .... Ты уверен, что хочешь сыграть со мной? Я не очень силен в играх ..... ")
    print()
    enter_game = input("Как будешь готов выйграть меня нажми Enter ...... ")
    print()
    if (queue_1 == 1 and queue_2 == 3) or (queue_1 == 1 and queue_2 == 4):
        os.system('cs||clear')
        print("Судьба распорядилась следующим псевдослучайным образом!")
        print()
        print("(I_o) Первым ходит", player_name)
        first = player_name
        print()
        print("(-_p) Второй ход за", bot_name)
        print()
        print('Удачной игры!')
        second = bot_name
        time.sleep(4)
        Start(first,second)
    else:
        os.system('cs||clear')
        print("Судьба распорядилась следующим псевдослучайным образом!")
        print()
        print("(I_o) Первым ходит", bot_name)
        first = bot_name
        print()
        print("(-_p) Второй ход за", player_name)
        second = player_name
        print()
        print('Удачной игры!')
        time.sleep(4)
        Start(first,second)