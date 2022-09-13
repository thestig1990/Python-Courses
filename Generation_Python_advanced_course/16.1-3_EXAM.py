import operator
from functools import reduce
from re import I


data = [1, 2, 10, 23, 123, 3000]
side='-'
print('', side * (len(data)*3 - 1))


print(dir(operator))
help(operator.concat)

print([1,2,3] + [])

def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)


print(product_of_odds([1, 2, 3]))


words = 'the world is mine take a look what you have started'.split()

print(*list(map(lambda x: f'"{x}"', words)), sep=' ')


ip_list = [['128', '199', '44', '24'], ['128', '199', '201', '245'], ['143', '198', '168', '95'], ['172', '67', '181', '62'], ['172', '67', '222', '111'], ['172', '67', '10', '90'], ['45', '8', '106', '59'], ['203', '13', '32', '156'], ['172', '67', '181', '194']]


ip_list_mod = []

for i in range(len(ip_list)):
    ip_10 = 0
    for j in range(len(ip_list[i])):
        ip_10 += (int(ip_list[i][j]) * (256**(len(ip_list[i]) - j - 1)))
    ip_list_mod.append(ip_10)


print(ip_list_mod)
print(sorted(ip_list_mod))

l_m = list(zip(ip_list, ip_list_mod))
l_n_sort = sorted(l_m, key=lambda x: x[1])

for i in l_n_sort:
    print('.'.join(i[0]))

print(ip_list)
L_sort = [[i for i in j] for j in ip_list]


print()
print(L_sort)

for i in L_sort:
    print('.'.join(i))



from operator import add, sub, mul, truediv

def arithmetic_operation(operation):
    def func(x, y):
        result = {'+': add, '-': sub, '*': mul, '/': truediv}
        return result[operation](x, y)
    return func

print(arithmetic_operation('/')(20, 5))