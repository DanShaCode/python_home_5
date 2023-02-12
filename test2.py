my_list = ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

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

print()     
print(result_counter)
        
