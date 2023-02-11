import re

def Abc_Remover(text):
    change_text = [re.sub("[абв]", "", text)]
    print()
    print("Отредактированный текст: ", *change_text)