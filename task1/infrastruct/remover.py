import os

def ABC_Remover():
    os.system('cs||clear')
    print()
    print("Здравствуйте! Данная программа убирает из текста все слова где содержится 'абв'.")
    print()

    text = str(input("Введите, пожалуйста, текст: "))

    os.system('cs||clear')

    print()
    print("Текст, который вы ввели: ", text)
    print()

    text_in_list = text.split()
    filtered_text = []

    for word in text_in_list:
        if 'абв' in word:
            continue
        else:
            filtered_text.append(word)

    print("Отфильтрованный текст: ", *filtered_text)
    text_in_list.clear()