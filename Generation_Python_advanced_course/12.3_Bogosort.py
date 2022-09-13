# Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь
# фигуры, задаваемой с помощью системы неравенств:

import random

n = 10**6       # количество испытаний
k = 0
S_0 = 4*4

for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1

print((k/n) * S_0)


# Напишите программу, которая при помощи метода Монте-Карло определяет
# приближённое значение числа π.

# Примечание 1. Площадь единичного круга, то есть круга с радиусом, равным
# R=1 равна S = πR^2 =π.

# Примечание 2. Уравнение единичной окружности имеет вид x^2+y^2 = 1

n = 10**6       # количество испытаний
k = 0
S_0 = 4

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        k += 1

print((k/n) * S_0)


# Реализация алгоритма Болотная сортировка (Bogosort)

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):                  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        random.shuffle(nums)
    return nums


numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)                # выводим отсортированный список
