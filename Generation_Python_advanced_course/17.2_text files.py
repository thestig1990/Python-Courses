# file_name = '17.2_file.txt'
# file = open(file_name, 'r', encoding='utf-8')

# file_content = file.read()
# print(file_content)

# file.close()



# import random

# file1 = open('lines.txt', 'r', encoding='utf-8')

# file_content = file1.readlines()

# print(random.choice(file_content))

# file1.close()

# file_name = 'numbers.txt'

# file = open(file_name, 'r',encoding='utf-8')

# list_num = file.readlines()

# print(sum([int(i) for i in list_num]))

# file_name = 'nums.txt'

# file = open(file_name, 'r',encoding='utf-8')

# print(file.read().split())

# print(sum([int(i) for i in file.read().split()]))


file_name = 'prices.txt'

file = open(file_name, 'r',encoding='utf-8')

file_content = file.readlines()

list_content = [i.split() for i in file_content]

summ = 0
for i in list_content:
    summ += int(i[1]) * int(i[2])
    
print(summ)

