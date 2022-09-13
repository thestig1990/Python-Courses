# print(*[int(i)**2 for i in input().split() if int(i) %
# 2 == 0 and int(i)**2 % 10 != 4])
# if int(i) % 2 == 0 and int(i) % 10 != 4

# Пузырьковая сортировка без оптимизации
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
counter = 0
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            counter += 1

print(a, counter)

# Пузырьковая сортировка с оптимизацией
# Вариант 1
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
counter = 0
for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
            a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
            flag = False
            counter += 1
    if flag:
        break
print(a, counter)


# Пузырьковая сортировка с оптимизацией
# Вариант 2
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
counter = 0
for i in range(n - 1):
    flag = False
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
            a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
            flag = True
            counter += 1
    if flag == False:
        break
print(a, counter)


# Мы можем реализовать пузырьковую сортировку в Python
# следующим образом с использованием ф-ци:
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # Swap the elements
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    # Set the flag to True so we'll loop again
                    swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)


# Мы можем реализовать пузырьковую сортировку в Python
# следующим образом без использования ф-ци(ВАРИАНТ 1):
random_list = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
l = len(random_list)
counter = 0
swapped = True
for i in range(l - 1):
    if swapped == False:
        break
    for j in range(l - i - 1):
        if random_list[j] > random_list[j + 1]:
            # Swap the elements
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
            swapped = True
            counter += 1
# Verify it works
print(random_list, counter)


# Мы можем реализовать пузырьковую сортировку в Python
# следующим образом без использования ф-ци(ВАРИАНТ 2):
random_list = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
l = len(random_list)
counter = 0
for i in range(l - 1):
    swap = True
    for j in range(l - i - 1):
        if random_list[j] > random_list[j + 1]:
            # Swap the elements
            random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
            swap = False
            counter += 1
    if swap:
        break
# Verify it works
print(random_list, counter)
