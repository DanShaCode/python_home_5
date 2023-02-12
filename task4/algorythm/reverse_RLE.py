import os

os.system('cs||clear')

text = '5A5B'

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

numbers = [i for i in my_list if type(i) == int]
words = [i for i in my_list if type(i) == str]

print()
print("Числа: ", numbers)

print()
print("Строки: ", words)

result_list = []

count = 0
index = 0

for i in numbers:
    while count < i:
        result_list.append(words[index])
        count += 1
    index += 1
    count = 0

print()
print(''.join(result_list))
