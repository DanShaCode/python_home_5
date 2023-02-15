import os
from algorythm.RLE import *
from algorythm.reverse_RLE import *

os.system('cs||clear')
print()
print("Данная программа сжимает данные через алгоритм RLE, а затем эти данные восстанавливает.")
print()
text = str(input("Введите, пожалуйста, текст, который ВЫ хотите сжать: "))

rls_text = Run_Length_Encoding(text)

print()
user_ask = input("Нажмите Enter, чтобы восстановить текст ... ")

Reverse_RLS(rls_text)