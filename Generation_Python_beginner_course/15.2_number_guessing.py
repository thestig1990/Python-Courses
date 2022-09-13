# from random import randint
# def know_digit():
#     left = 1
#     right = n
#     middle = (left+right)//2
#     count = 1
#     while middle != num:
#         middle = (left+right)//2
#         if middle < num:
#             left = middle+1
#             count += 1
#         elif middle > num:
#             right = middle-1
#             count += 1
#     print("Количество попыток :", count)
#     return middle


# n = int(input())  # предел поискового диапозона
# num = int(input())  # называемое число
# print("Ваше число:", know_digit())

# from random import *
# print('Угадай число!')
# start = 1
# end = 1000
# middle = (start + end) // 2
# num = randint(1, 1000)
# while True:
#     if middle > num:
#         print('Число', str(middle), 'слишком большое!')
#         end = middle - 1
#         middle = (start + end) // 2
#     if middle < num:
#         print('Число', str(middle), 'слишком маленькое!')
#         start = middle + 1
#         middle = (start + end) // 2
#     else:
#         print('Вы угадали, поздравляем! Это число:', str(middle))
#         break


# импорт модуля random
import random
# генерирование случайного числа от 1 до right border
right_border = input(
    'Введите правую границу для выбора случайного числа(от 1 до n): ')
random_number = random.randint(1, int(right_border))
print('Добро пожаловать в числовую угадайку')


def is_valid(num):                           # ф-ция проверки числа
    if num.isdigit and 1 <= int(num) <= 100:
        return True
    else:
        return False


counter = 0
while True:
    n = input(f'Введите число от 1 до {right_border}: ')
    if not is_valid(n):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        n = int(n)
        if n < random_number:
            counter += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > random_number:
            counter += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif n == random_number:
            print('Вы угадали, поздравляем!', ', Число  попыток = ', counter)
        # print(n)
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся')
