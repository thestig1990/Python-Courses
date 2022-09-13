from random import choice
from random import sample
import string
import random


# IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно)
# разделенных точкой.
# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и
# возвращает случайный корректный IP адрес.


def generate_ip():
    list_num = list(range(256))
    list_ip_num = random.sample(list_num, 4)
    list_ip = [str(i) for i in list_ip_num]
    ip = '.'.join(list_ip)
    return ip


print(generate_ip())


# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter,
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99.

# Напишите функцию generate_index, которая с помощью модуля random генерирует
# и возвращает случайный корректный почтовый индекс Латверии.


# import string
# import random

def generate_index():
    list_firstpart = []
    list_secondtpart = []

    for _ in range(3):
        if len(list_firstpart) < 2:
            list_firstpart.append(random.choice(string.ascii_uppercase))
        else:
            list_firstpart.append(random.randrange(100))

    for _ in range(3):
        if len(list_secondtpart) < 1:
            list_secondtpart.append(random.randrange(100))
        else:
            list_secondtpart.append(random.choice(string.ascii_uppercase))

    list_firstpart_adress = [str(i) for i in list_firstpart]
    list_secondtpart_adress = [str(i) for i in list_secondtpart]

    firstpart_adress = ''.join(list_firstpart_adress)
    secondtpart_adress = ''.join(list_secondtpart_adress)
    post_adress = firstpart_adress + '_' + secondtpart_adress
    return post_adress


print(generate_index())


# Напишите программу, которая с помощью модуля random перемешивает случайным
# образом содержимое матрицы (двумерного списка).


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print(random.shuffle(matrix))


# Напишите программу, которая с помощью модуля random генерирует 100 случайных
# номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите
# внимание, вы должны придерживаться следующих условий:

# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 77 цифр;
# все 100100 лотерейных билетов должны быть различными.


for _ in range(100):
    print(random.randint(1000000, 9999999))


# Анаграмма – это слово образованное путём перестановки букв, составляющих
# другое слово.
# Например, слова пила и липа или пост и стоп – анаграммы.
# Напишите программу, которая считывает одно слово и выводит с помощью модуля
# random его случайную анаграмму.
# Примечание. Обратите внимание на то, что метод shuffle() работает со списком,
# а не со строкой.


word = 'пила'

L = []
for c in word:
    L.append(c)

random.shuffle(L)
Anagram = ''.join(L)
print(Anagram)


# Генератор паролей 1
# Напишите программу, которая с помощью модуля random генерирует nn паролей
# длиной mm символов, состоящих из строчных и прописных английских букв и цифр,
# кроме тех, которые легко перепутать между собой:

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с
# условием задачи, каждый на отдельной строке


def generate_password(length):
    LETTER = ' '.join((set(string.ascii_letters) |
                      set(string.digits)) - set('lI1oO0'))
    return ''.join(random.sample(LETTER.split(), length))


def generate_passwords(count, length):
    password_list = []
    for _ in range(count):
        password_list.append(generate_password(length))
    return password_list


n, m = 9, 7

print(*generate_passwords(n, m), sep='\n')


# Для игры в бинго требуется карточка размером 5×5, содержащая различные
# (уникальные) целые числа от 11 до 7575 (включительно), при этом
# центральная клетка является пустой (она заполняется числом 0).

# Напишите программу, которая с помощью модуля random генерирует и выводит
# случайную карточку для игры в бинго.


# VAR1
numbers_list = [str(i) for i in range(1, 76)]

numbers_bingo = random.sample(numbers_list, 25)

numbers_bingo[12] = '0'

count = 0
for i in range(len(numbers_bingo)):
    count += 1
    if count == 6 or count == 11 or count == 16 or count == 21:
        print()
    print(numbers_bingo[i].ljust(4), end='')


# VAR2
numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()


# Тайный друг 🌶️
# Напишите программу, которая случайным образом назначает каждому ученику его
# тайного друга, который будет вместе с ним решать задачи по программированию.

# Формат входных данных
# На вход программе в первой строке подается число n – общее количество
# учеников. Далее идут n строк, содержащих имена и фамилии учеников.

# Формат выходных данных
# Программа должна вывести имя и фамилию ученика (в соответствии с исходным
# порядком) и имя и фамилию его тайного друга, разделённые дефисом.


# VAR1
# names_list = [input() for _ in range(int(input()))]

# for i in range(len(names_list)):
#     if i == len(names_list) - 1:
#         print(names_list[i], '-', names_list[0])
#     else:
#         print(names_list[i], '-', names_list[i+1])


# VAR2

# names, rel, tmp = {input() for _ in range(int(input()))}, {}, 0
# for name in names.copy():
#     if names == {name}:
#         rel[tmp], rel[name] = name, rel[tmp]
#     else:
#         rand_name = choice(list(names - {name}))
#         rel[name] = rand_name
#         names -= {rand_name}
#         tmp = name
# [print(k, '-', v) for k, v in rel.items()]


# Генератор паролей 2 🌶️
# Напишите программу, которая с помощью модуля random генерирует n паролей
# длиной m символов, состоящих из строчных и прописных английских букв и цифр,
# кроме тех, которые легко перепутать между собой:

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Дополнительное условие: в каждом пароле обязательно должна присутствовать
# хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с
# условием задачи, каждый на отдельной строке.

# VAR1
def generate_password(length):
    LETTER = ' '.join(set(string.ascii_uppercase) - set('IO'))
    letter = ' '.join(set(string.ascii_lowercase) - set('lo'))
    dig = ' '.join(set(string.digits) - set('01'))
    ALL_LETTER = ' '.join((set(string.ascii_letters) |
                           set(string.digits)) - set('lI1oO0'))
    return (''.join(random.sample(LETTER.split(), 1)) +
            ''.join(random.sample(letter.split(), 1)) +
            ''.join(random.sample(dig.split(), 1)) +
            ''.join(random.sample(ALL_LETTER.split(), length - 3)))


def generate_passwords(count, length):
    password_list = []
    for _ in range(count):
        password_list.append(generate_password(length))
    return password_list


n, m = 9, 7

print(*generate_passwords(n, m), sep='\n')

print()


# VAR2
def generate_password(length):
    LETTER = set(string.ascii_uppercase) - set('IO')
    letter = set(string.ascii_lowercase) - set('lo')
    dig = set(string.digits) - set('01')
    ALL_LETTER = ' '.join((set(string.ascii_letters) |
                           set(string.digits)) - set('lI1oO0'))
    while True:
        password = ''.join(random.sample(ALL_LETTER.split(), length))
        if (len(set(password) & LETTER) > 0 and len(set(password) & letter) > 0
                and len(set(password) & dig) > 0):
            break
    return password


def generate_passwords(count, length):
    password_list = []
    for _ in range(count):
        password_list.append(generate_password(length))
    return password_list


n, m = 9, 7

print(*generate_passwords(n, m), sep='\n')
