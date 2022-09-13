# Напишите функцию func, используя синтаксис анонимных функций, которая
# принимает целочисленный аргумент и возвращает значение True, если он
# делится без остатка на 19 или на 13 и False в противном случае.

from functools import reduce
def func(x): return True if x % 19 == 0 or x % 13 == 0 else False


print(func(13))
print(func(15))
print(func(19))


# Напишите функцию func, используя синтаксис анонимных функций, которая
# принимает строковый аргумент и возвращает значение True, если переданный
# аргумент начинается и заканчивается на английскую букву a (регистр буквы
# неважен) и False в противном случае.

def func(string): return True if string.lower().endswith(
    'a') and string.lower().startswith('a') else False


print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))


# Напишите функцию is_non_negative_num, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True, если
# переданный аргумент является неотрицательным числом (целым или вещественным)
# и False в противном случае.

def is_non_negative_num(num): return True if num.count(
    '.') <= 1 and num.replace('.', '').isdigit() and float(num) >= 0 else False


print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))


# Напишите функцию is_num, используя синтаксис анонимных функций, которая
# принимает строковый аргумент и возвращает значение True, если переданный
# аргумент является числом (целым или вещественным) и False в противном случае.

def is_num(num): return True if '-' not in num[1:] and num.count(
    '.') <= 1 and num.replace('.', '').replace('-', '').isdigit() else False


print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))


# Напишите программу, которая с помощью встроенных функций filter() и sorted()
# выводит слова из списка words, имеющие длину ровно 66 символов. Слова
# следует вывести в алфавитном порядке на одной строке, разделив символом
# пробела.

words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse',
         'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct',
         'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow',
         'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard',
         'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday',
         'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle',
         'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday',
         'accessory', 'absorb']

filter_words = list(filter(lambda word: len(word) == 6, words))

print(*sorted(filter_words), sep=' ')


# Напишите программу, которая с помощью встроенных функций map() и filter()
# удаляет из списка numbers все нечетные элементы, большие 47, а все четные
# элементы нацело делит на два (целочисленное деление – //). Полученные числа
# следует вывести на одной строке, разделив символом пробела и сохранив
# исходный порядок.

numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34,
           100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16,
           40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49,
           78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95,
           90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44,
           2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

func_filter = list(filter(lambda num: not (
    num > 47 and num % 2 != 0), numbers))

func_map = list(map(lambda num: num // 2 if num %
                2 == 0 else num, func_filter))

print(*func_map, sep=' ')


# Список data содержит информацию о численности населения некоторых штатов США.
# Напишите программу сортировки по убыванию списка data на основании последнего
# символа в названии штата. Затем распечатайте элементы этого списка, каждый на
# новой строке в формате:

# <название штата>: <численность населения>

# Vermont: 626299
# Massachusetts: 7029917

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'),
        (626299, 'Vermont'), (1805832, 'West Virginia'),
        (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'),
        (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

data_sort = sorted(data, key=lambda x: x[1][-1], reverse=True)

for i in data_sort:
    print(i[1] + ':', i[0])


# Список data содержит слова на русском языке. Напишите программу его
# сортировки по возрастанию длины слов, а затем в лексикографическом порядке.
# Отсортированные слова следует вывести на одной строке, разделив символом
# пробела.

# Примечание 1. Используйте анонимную функцию в качестве критерия сортировки.

# Примечание 2. Если длина слов совпадает, сортировать нужно в
# лексикографическом порядке.


data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз',
        'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом',
        'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
        'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина',
        'деньги']

data_sort = sorted(data, key=lambda x: (len(x), x))

print(*data_sort, sep=' ')


# Список mixed_list содержит целочисленные и строковые значения. Напишите
# программу, которая с помощью встроенной функции max() находит и выводит
# наибольшее числовое значение в указанном списке.

# Примечание 1. Для решения задачи используйте анонимную функцию и
# необязательный аргумент key  функции max().

# Примечание 2. Обратите внимание, что сравнивать числа и строки нельзя.

mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate',
              'accessory', 'absorb', 1384878, 'sunday', 'about', 454805,
              'saturday', 'abort', 2121919, 2552839, 977970, 1772933,
              1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate',
              1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665,
              'besides', 'bewilder', 1586517, 375290, 1503450, 2713047,
              'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280,
              686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident',
              2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113,
              1618068, 'berth', 'abolish', 'beware', 2618492, 1555062,
              'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
              'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday',
              810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse',
              'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320,
              2347441]


maximum = max(mixed_list, key=lambda x: (type(x) == int, x))

print(maximum)


# Список mixed_list содержит целочисленные и строковые значения. Напишите
# программу его сортировки по неубыванию значений элементов, при этом
# числа должны следовать до строк.  Элементы отсортированного списка
# выведите на одной строке, разделив символом пробела.

# Примечание 1. Для решения задачи используйте анонимную функцию и
# необязательный аргумент key  функции sorted().

# Примечание 2. Если бы список mixed_list содержал значения:

mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides',
              'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36,
              'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday',
              87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident',
              'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
              'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65,
              51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46,
              'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95,
              'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday',
              66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

mixed_list_num = list(filter(lambda x: type(x) == int, mixed_list))
mixed_list_word = list(filter(lambda x: type(x) == str, mixed_list))

mixed_list_new = sorted(mixed_list_num) + sorted(mixed_list_word)

print(*mixed_list_new)


# Противоположный цвет
# В цветовой схеме RGB цвета задаются с помощью трех компонентов:

# R — интенсивность красной составляющей цвета;
# G — интенсивность зеленой составляющей цвета;
# B — интенсивность синей составляющей цвета.
# Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B).
# Считается, что такие цвета хорошо гармонируют друг с другом.

# Напишите программу, которая по трем компонентам заданного цвета, находит
# компоненты противоположного цвета.

# Формат входных данных
# На вход программе подается строка, содержащая три целых неотрицательных
# числа, компоненты R, G и B начального цвета,  разделенные символом пробела.

# Формат выходных данных
# Программа должна вывести три компонента R, G и B противоположного цвета,
# разделенные символом пробела.

# Примечание. Попробуйте решить задачу в одну строку с помощью встроенной
# функции map().

s = input().split()

opposite_color = list(map(lambda x: 255 - int(x), s))

print(*opposite_color)


# Значение многочлена 🌶️


coefficient = input().split()
x = int(input())

coefficient_int = [int(i) for i in coefficient]


def evaluate(coefficients, x):
    list_degree = list(range(len(coefficients)))[::-1]
    eval1 = list(map(lambda a, b: a*x**b, coefficients, list_degree))
    return reduce(lambda x, y: x + y, eval1)


print(evaluate(coefficient_int, x))
