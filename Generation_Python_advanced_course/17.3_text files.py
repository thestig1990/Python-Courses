with open('input.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')
        


with open('text.txt', encoding='utf-8') as file:
    print(file.readline()[::-1])


with open('data.txt', encoding='utf-8') as file:
    data = list(map(str.strip, file.readlines()))
    print(*data[::-1], sep='\n')


print(max(['juice', 'pizza']))


with open('lines.txt', encoding='utf-8') as file:
    list_lines =  list(map(str.strip, file.readlines()))
    max_len = len(max(list_lines, key=len))
    list_max = [i for i in list_lines if len(i) == max_len]
    print(*list_max, sep='\n')


with open('numbers.txt', encoding='utf-8') as file:
    for string in file:
        print(sum([int(i) for i in string.split()]), end='\n')



with open('nums.txt', encoding='utf-8') as file:
    str_num = ''
    for line in file:
        for c in line:
            if c.isdigit():
                str_num += c
            else:
                str_num += ' '
        
print(sum(map(int, str_num.split())))


with open('file.txt', encoding='utf-8') as file:
    count_line = len(file.readlines())
    file.seek(0)
    list_line = list(map(str.strip, file.readlines()))
    count_word = sum([len(i.split()) for i in list_line])
    count_alpha = 0
    for i in list_line:
        for j in i:
            if j.isalpha():
                count_alpha +=1                     
    print('Input file contains:', str(count_alpha) + ' letters', str(count_word) + ' words', str(count_line) + ' lines', sep='\n')




from random import choice

with open('first_names.txt', encoding='utf-8') as names, open('last_names.txt', encoding='utf-8') as l_names:
    list_names = list(map(str.strip, names.readlines()))
    list_l_names = list(map(str.strip, l_names.readlines()))
    n = 3
    while n > 0:
        print(choice(list_names), choice(list_l_names))
        n -= 1



with open('population.txt', encoding='utf-8') as file:
    for line in file:
        country = line.split()
        if country[0][0] == 'G' and int(country[-1]) > 500000:
            print(country[0])



with open('data.csv', encoding='utf-8') as file:
    list_line = list(map(str.strip, file.readlines()))
    list_data = [i.split(',') for i in list_line]
    list_key = list_data[0]
    list_value = list_data[1:]
    print(list_key)
    print(list_value)
    
def read_csv():
    L = []
    for i in range(len(list_value)):
        d = {}
        key, value = list_key, list_value
        for j in range(len(list_value[i])):
            d[key[j]] = value[i][j]
        L.append(d)   
    return L

print(read_csv())