import os

os.system('cs||clear')

text = 'aabbaaabbbcccbbbcccc'

my_list = []

for char in text:
    my_list.append(char)

print()
print(my_list)
print()

my_list.sort()

# for i in my_list:
#     print(ord(i), i, end = ' ')

# symbol_counter = {}

# print()
# print()
# print(RLE(my_list,symbol_counter))
# print()
# print(symbol_counter)