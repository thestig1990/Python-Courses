with open('input.txt', 'r', encoding='utf-8') as input:
    list_lines = input.readlines()
    print(list_lines)

with open('output.txt', 'w', encoding='utf-8') as output:
    for line in enumerate(list_lines, 1):
        output.write(str(line[0]) + ') ' + line[1])


with open('class_scores.txt', 'r', encoding='utf-8') as class_scores:
    list_scores = list(map(str.strip, class_scores.readlines()))
    list_scores_new = [i.split() for i in list_scores]


with open('new_scores.txt', 'w', encoding='utf-8') as new:
    for line in list_scores_new:
        if int(line[1]) <= 95:
            new.write(line[0] + ' ' + str(int(line[1]) + 5) + '\n')
        else:
            new.write(line[0] + ' 100\n')


with open('ledger.txt', encoding='utf-8') as file:
    list_strig = list(map(str.strip, file.readlines()))
    list_num = [int(i[1:]) for i in list_strig]
    print(list_strig[0][0], sum(list_num), sep='')


with open('grades.txt', encoding='utf-8') as file:
    list_string = list(map(str.strip, file.readlines()))
    list_string_new = [i.split() for i in list_string]
    num_students = 0
    for i in list_string_new:
        total = 0
        for j in i:
            if j.isdigit() and int(j) >= 65:
                total += 1
        if total == 3:
            num_students += 1
    print(num_students)


with open('words.txt', encoding='utf-8') as file:
    list_words = list(map(str.strip, file.read().split()))
    for i in list_words:
        if len(i) == len(max(list_words, key=len)):
            print(i)


file_name = 'lines.txt'
with open(file_name, encoding='utf-8') as file:
    list_file = list(file)
    if len(list_file) == 10:
        print(*list_file, sep='')
    else:
        list_file_10 = list_file[:-11:-1]
        print(*list_file_10[::-1], sep='')


# trans = '''
# а     a     к     k     х     h
# б     b     л     l     ц     c
# в     v     м     m     ч     ch
# г     g     н     n     ш     sh
# д     d     о     o     щ     shh
# е     e     п     p     ъ     *
# ё     jo    р     r     ы     y
# ж     zh    с     s     ь     '
# з     z     т     t     э     je
# и     i     у     u     ю     ju
# й     j     ф     f     я     ya'''.split()

# abc_dict = dict(zip([trans[i] for i in range(0, len(trans), 2)],
#                     [trans[i] for i in range(1, len(trans), 2)]))

# abc_dict.update(zip([trans[i].upper() for i in range(0, len(trans), 2)],
#                     [trans[i].title() for i in range(1, len(trans), 2)]))

# for key in abc_dict:
#     print(f'{key}: {abc_dict[key]}')


with open('cyrillic.txt', encoding='utf-8') as file:
    symbol = file.read()

L = []

d = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v',
     'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o',
     'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y',
     'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i',
     'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
     'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V',
     'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O',
     'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y',
     'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I',
     'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'}

for i in symbol:
    for j in range(len(i)):
        if i[j] in d:
            L.append(i[j].replace(i[j], d[i[j]]))
        else:
            L.append(i[j])

str_1 = ''.join(L)
new = str_1.split('\n')

with open('transliteration.txt', 'w', encoding='utf-8') as f:
    print(*new, sep='\n', file=f)


print([1]*6)
help(round)

print(round(1.11510, 2))


keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

print(list(zip(keys, values)))
info = dict(zip(keys, values))
print(info)