# Минутка генетики
# Как известно из курса биологии ДНК и РНК – последовательности
# нуклеотидов.

# Цепь РНК строится на основе цепи ДНК последовательным присоединением
# комплементарных нуклеотидов:
# G → C;
# C → G;
# T → A;
# A → U.
# Напишите программу, переводящую цепь ДНК в цепь РНК.

DNA = input()

RNA_convert = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

rna_string = ''

for c in DNA:
    rna_string += RNA_convert[c]
print(rna_string)


# Порядковый номер
# Дана строка текста на русском языке, состоящая из слов и символов
# пробела. Словом считается последовательность букв, слова разделены
# одним пробелом или несколькими.

# Напишите программу, определяющую для каждого слова порядковый номер
# его вхождения в текст именно в этой форме, с учетом регистра. Для
# первого вхождения слова программа выведет 1, для второго вхождения
# того же слова — 2 и т. д.

my_list = input().split(' ')

result = {}

for c in my_list:
    result[c] = result.get(c, 0) + 1
    print(result[c], end=' ')


# Scrabble game
# В игре Scrabble каждая буква приносит определенное количество баллов.
# Общая стоимость слова – сумма баллов его букв. Чем реже буква
# встречается, тем больше она ценится:
# Напишите программу подсчета итоговой стоимости введенного слова.

word = input()

my_dict = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

value_word = 0

for c in word:
    for key in my_dict:
        if c in my_dict[key]:
            value_word += key

print(value_word)


# Строка запроса
# Строка запроса (query string) — часть URL адреса, содержащая ключи и
# их значения. Она начинается после вопросительного знака и идет до
# конца адреса. Например:
# https://beegeek.ru?name=timur     # строка запроса: name=timur
# Если параметров в строке запроса несколько, то они отделяются символом
# амперсанда &:
# https://beegeek.ru?name=timur&color=green
# строка запроса: name=timur&color=green
# Напишите функцию build_query_string(), которая принимает на вход
# словарь с параметрами и возвращает строку запроса, сформированную из
# этих параметров.

def build_query_string(params):
    sorted_keys = sorted(params)
    result = []
    for key in sorted_keys:
        result.append(key + '=' + str(params[key]))
    return '&'.join(result)


print(build_query_string({'name': 'timur', 'age': 28}))


# Слияние словарей 🌶️
# Напишите функцию merge(), объединяющую словари в один общий.
# Функция должна принимать список словарей и возвращать словарь, каждый
# ключ которого содержит множество (тип данных set) уникальных значений
# собранных из всех словарей переданного списка.


def merge(values):      # values - это список словарей
    my_dict = {}
    for dict1 in values:
        for key, value in dict1.items():
            my_dict.setdefault(key, set())
            my_dict[key].add(value)
    return my_dict


print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {
      'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))


# Опасный вирус 😈
# В файловую систему компьютера, на котором развернута наша ❤️ платформа
# Stepik, проник опасный вирус и сломал контроль прав доступа к файлам.
# Говорят, вирус написал один из студентов курса Python для начинающих.

# Для каждого файла известно, с какими действиями можно к нему обращаться:

# запись W (write, доступ на запись в файл);
# чтение R (read, доступ на чтение из файла);
# запуск X (execute, запуск на исполнение файла).
# Напишите программу для восстановления контроля прав доступа к файлам.
# Ваша программа для каждого запроса должна будет возвращать OK если
# выполняется допустимая операция, и Access denied, если операция
# недопустима.

my_dict1 = {'write': 'W', 'read': 'R', 'execute': 'X'}

my_dict2 = {}
for i in range(int(input())):
    s = input().split()
    my_dict2[s[0]] = tuple(s[1:])

for i in range(int(input())):
    s = input().split()
    if my_dict1[s[0]] in my_dict2[s[1]]:
        print('OK')
    else:
        print('Access denied')
