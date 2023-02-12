import os
from algorythm.RLE import *
from algorythm.reverse_RLE import *

os.system('cs||clear')
print()
text = str(input("Введите, пожалуйста, текст: "))

rls_text = Run_Length_Encoding(text)

print()
user_ask = input("Нажмите Enter, чтобы восстановить текст ... ")

Reverse_RLS(rls_text)