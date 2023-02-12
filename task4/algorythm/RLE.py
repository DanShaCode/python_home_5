import os

os.system('cs||clear')

def RLE(my_list, symbol_counter):
    if len(my_list) == 0:
        return symbol_counter
    else:
        count = 0
        index = 0
        list_len = len(my_list) - 1
        symbol_amount = 0
        while count < list_len:
            if my_list[index] == my_list[index+1]:
                print('Yes', my_list[index], end = ' ')
                index +=1
                count +=1
                symbol_amount += 1
            else:
                symbol_amount += 1
                symbol_counter [symbol_amount] = my_list[index]
                del my_list [:index+1] 
                return RLE(my_list, symbol_counter)

text = 'aabbaaabbbcccbbbcccc'

my_list = []

for char in text:
    my_list.append(char)

print()
print(my_list)
print()

my_list.sort()

for i in my_list:
    print(ord(i), i, end = ' ')

symbol_counter = {}

print()
print()
print(RLE(my_list,symbol_counter))
print()
print(symbol_counter)