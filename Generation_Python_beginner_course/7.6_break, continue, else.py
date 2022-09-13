for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)


for i in range(10):
    print(i, end='*')
    if i > 6:
        break


i = 3
print(i % 9, end=' ')
