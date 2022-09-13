# def do_something():
#     a = 1
#     print(a)
# a = 0
# do_something()
# print(a)


# a = 1
# def do_something():
#     print(a)
# do_something()


# def do_something():
#     a = 1
# do_something()
# print(a)


# h_triangle = 8
# symbol = '*'
# for i in range(h_triangle):
#     print(' ' * (h_triangle - i - 1) + symbol * (1 + i*2))


# Звездный треугольник 🌶️
# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный
# треугольник с основанием и высотой равными 1515 и 88 соответственно:

# # объявление функции
# def draw_triangle(h, symb):
#     for i in range(h):
#         print(' ' * (h - i - 1) + symb * (1 + i*2))


# h_triangle = 8
# symbol = '*'
# # вызов функции
# draw_triangle(h_triangle, symbol)


# Калькулятор доставки
# Интернет магазин осуществляет экспресс доставку для своих товаров по цене
# 10001000 рублей за первый товар и 120120 рублей за каждый последующий
# товар. Напишите функцию get_shipping_cost(quantity), которая принимает
# в качестве аргумента натуральное число quantity – количество товаров в
# заказе и возвращает стоимость доставки.

# # объявление функции
# def get_shipping_cost(quantity):
#     total_cost = 1000
#     if quantity == 1:
#         total_cost = total_cost
#     for i in range(quantity-1):
#         total_cost += 120
#     return total_cost


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_shipping_cost(n))


# Искомый месяц
# Напишите функцию get_month(language, number), которая принимает на вход
# два аргумента language – язык ru или en и number – номер месяца(от 1 до 12)
# и возвращает название месяца на русском или английском языке.


# # объявление функции
# def get_month(language, number):
#     lst_month_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#                     'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lst_month_en = ['january', 'february', 'march', 'april', 'may', 'june',
#                     'july', 'august', 'september', 'october', 'november', 'december']
#     if language == 'ru':
#         return lst_month_ru[number-1]
#     elif language == 'en':
#         return lst_month_en[number-1]


# # считываем данные
# lan = input()
# num = int(input())

# # вызываем функцию
# print(get_month(lan, num))


# Магические даты
# Магическая дата – это дата, когда день, умноженный на месяц, равен числу
# образованному последними двумя цифрами года.
# Напишите функцию, is_magic(date) которая принимает в качестве аргумента
# строковое представление корректой даты и возвращает значение True если
# дата является магической и False в противном случае.

# # объявление функции
# def is_magic(date):
#     lst = []
#     lst = date.split('.')
#     lst_n = lst.copy()
#     # return lst
#     # if int(lst[0]) < 10 and int(lst[1]) < 10:
#     for i in range(len(lst)):
#         lst_n[i] = int(lst_n[i])
#     if lst_n[0] * lst_n[1] == int(lst[2][2:]):
#         return True
#     else:
#         return False


# # считываем данные
# date = input()


# # вызываем функцию
# print(is_magic(date))


# Панграммы
# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно
# панграммы используют для презентации шрифтов, чтобы можно было в одной
# фразе рассмотреть все глифы.
# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента
# строку текста на английском языке и возвращает значение True если текст
# является панграммой и False в противном случае.
# Примечание 1. Гарантируется, что введенная строка содержит только буквы
# английского алфавита.


# # объявление функции
# def is_pangram(text):
#     text = text.lower()
#     # return text
#     alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
#                 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'v', 'b', 'n', 'm']
#     for i in range(len(text)):
#         if text[i] in alphabet:
#             alphabet.remove(text[i])
#     # return alphabet
#     if len(alphabet) == 0:
#         return True
#     else:
#         return False


# # считываем данные
# text = input()

# # вызываем функцию
# print(is_pangram(text))


# Биномиальный коэффициент 🌶️
# Напишите функцию compute_binom(n, k), которая принимает в качестве
# аргументов два натуральных числа n и k и возвращает значение биномиального
# коэффициента, равного \dfrac{n!}{k! (n-k)!}


# объявление функции
from math import factorial


def compute_binom(n, k):
    binom = factorial(n) / (factorial(k) * factorial(n - k))
    return int(binom)


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
