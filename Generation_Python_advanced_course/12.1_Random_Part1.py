# Напишите программу, которая с помощью модуля random моделирует броски монеты.
# Программа принимает на вход количество попыток и выводит результаты бросков:
# Орел или Решка (каждое на отдельной строке).

# Примечание. Например, при n=7 ваша программа может выводить:
# Орел
# Решка
# Решка
# Орел
# Орел
# Орел
# Решка

import random

n = int(input())    # количество попыток

for i in range(n):
    num = random.randrange(2)
    if num == 0:
        print('Орел')
    else:
        print('Решка')


# Напишите программу, которая с помощью модуля random моделирует броски
# игрального кубика c 66 гранями. Программа принимает на вход количество
# попыток и выводит результаты бросков — выпавшее число, которое написано
# на грани кубика (каждое на отдельной строке).

# import random
n = int(input())    # количество попыток

for _ in range(n):
    print(random.randint(1, 6))


# Напишите программу, которая с помощью модуля random генерирует случайный
# пароль. Программа принимает на вход длину пароля и выводит случайный пароль,
# содержащий только символы английского алфавита a..z, A..Z (в нижнем и
# верхнем регистре).

# import random
length = int(input())    # длина пароля

list_symbol = []

for _ in range(length):
    num1 = random.randint(65, 90)
    num2 = random.randint(97, 122)
    rand = random.randint(0, 1)
    if rand == 0:
        list_symbol.append(chr(num1))
    else:
        list_symbol.append(chr(num2))

print(*list_symbol, sep='')


# Лотерейный билет содержит 77 чисел из диапазона от 1 до 49 (включительно).
# Напишите программу, которая с помощью модуля random генерирует 77 различных
# случайных чисел для лотерейного билета. Программа должна вывести числа в
# порядке возрастания на одной строке через один символ пробела.

# import random
my_set = set()

while len(my_set) != 7:
    loterry_num = random.randrange(1, 50)
    my_set.add(loterry_num)

print(*sorted(my_set))
