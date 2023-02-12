
print()
text = str(input("Введите, пожалуйста, текст: "))

my_list = []

for char in text:
    my_list.append(char)

my_list.sort()

my_list.append('0')

symbol_counter = 0

counter = []

result_counter = {}

for i in range(len(my_list)-1):
    if str(ord(my_list[i])) == str(ord(my_list[i+1])):
        counter.append(str(my_list[i]))
        symbol_counter += 1
    else:
        symbol_counter += 1
        result_counter [my_list[i]] = symbol_counter
        symbol_counter = 0
        continue

result_list = []

for key,value in result_counter.items():
    result_list.append(str(value))
    result_list.append(str(key))

print()
print(''.join(result_list))