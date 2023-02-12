import os

os.system('cs||clear')

text = '4a5b'

print()
print("Изначальный текст: ", text)

my_list = []

for char in text:
    my_list.append(char)

print()
print("Отдельные символы в списке: ", my_list)

my_list_len = len(my_list)
count = 0

while count < my_list_len:
    if count % 2 == 0:
        my_list[count] = int(my_list[count])
        count += 1
    else:
        count += 1
        continue

print()
print("Числовые строки преобразованы в int: ", my_list)