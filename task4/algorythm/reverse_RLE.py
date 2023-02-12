import os

os.system('cs||clear')

def Reverse_RLS(text):
    words = []
    numbers = []

    for i in text:
        if i.isalpha():
            if not words or not last_isalpha:
                words.append(i)
            else:
                words[-1] += i
        else:
            if not numbers or last_isalpha:
                numbers.append(i)
            else:
                numbers[-1] += i
        last_isalpha = i.isalpha()

    numbers = [int(i) for i in numbers]
    words = [str(i) for i in words]

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
    print("Восстановленный текст: ", ''.join(result_list))
