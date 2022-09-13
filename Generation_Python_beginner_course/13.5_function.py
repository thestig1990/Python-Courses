# Is a Number Prime? 🌶️
# Напишите функцию is_prime(num), которая принимает в качестве аргумента
# натуральное число и возвращает значение True если число является простым и False
# в противном случае.

# Примечание. Следующий программный код:
# print(is_prime(1))
# должен выводить:
# False

# объявление функции
# def is_prime(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False


# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))


# def is_one_away(word1, word2):
#     if len(word1) == len(word2):
#         counter = 0
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 counter += 1
#         if counter == len(word1) - 1:
#             return True
#         else:
#             return False
#     else:
#         return False


# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))


# Good password 🌶️
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента
#  строковое значение пароля password и возвращает значение True если пароль является
# надежным и False в противном случае.

# Пароль является надежным если:
# его длина не менее 88 символов
# он содержит как минимум одну заглавную букву(верхний регистр)
# он содержит как минимум одну строчную букву(нижний регистр)
# он содержит хотя бы одну цифру.


# # объявление функции
# def is_password_good(password):
#     counter_isdigit = 0
#     counter_lower = 0
#     counter_upper = 0
#     if len(password) < 8:
#         return False
#     else:
#         for c in password:
#             if c.isdigit():
#                 counter_isdigit += 1
#             if c.islower():
#                 counter_lower += 1
#             if c.isupper():
#                 counter_upper += 1
#         if counter_isdigit >= 1 and counter_lower >= 1 and counter_upper >= 1:
#             return True
#         else:
#             return False


# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))


# Палиндром 🌶️
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку
# text и возвращает значение True если указанный текст является палиндромом и False
# в противном случае.

# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также
# игнорируйте пробелы, а также символы, . ! ? -.


# # объявление функции
# def is_palindrome(text):
#     lst = []
#     for i in range(len(text)):
#         if text[i].isalpha():
#             lst.append(text[i].lower())
#     if lst[:] == lst[::-1]:
#         return True
#     else:
#         return False

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_palindrome(txt))


# Змеиный регистр
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента
# строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

# Примечание 1. Почитать подробнее о стилях именования можно тут.
# Примечание 2. Следующий программный код:
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))

# должен выводить:
# this_is_camel_cased
# is_prime_number


# # объявление функции
# def convert_to_python_case(text):
#     s = text[0].lower()
# # print(s_1)

#     for c in text[1:]:
#         if c.isupper():
#             s = s + '_' + c.lower()
#         else:
#             s = s + c
#     return s


# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))

# text = '()(()())'
# text = text.replace('()', '')
# text = text.replace('()', '')
# print(text)


# объявление функции
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
        text = text.replace('()', '')
    if len(text) == 0:
        return True
    elif '()' not in text:
        return False
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
