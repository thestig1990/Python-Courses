from typing import overload


num = 12345
num_1 = str(num)
print(num_1, type(num_1))
num_2 = ' '.join(num_1)
print(num_2, type(num_2))
num_3 = num_2.split(' ')
print(num_3, type(num_3))
for i in range(len(num_3)):
    num_3[i] = int(num_3[i])
print(sum(num_3), type(num_3[:]))
