En_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
Ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'


language = input(
    'Какой язык использовать для де/шифрования? (En - "English", Ru - "Русский"): ').lower()
if language == 'en':
    lang_len, start, start_upper, end, end_upper = 26, 'a', 'A', 'z', 'Z'
if language == 'ru':
    lang_len, start, start_upper, end, end_upper = 32, 'а', 'А', 'я', 'Я'
# shift_step = int(input(
#     'Введите шаг сдвига(со сдвигом вправо). Для "Еn" - шаг от 0 до 26, для "Ru" - шаг от 0 до 32: '))
de_encryption = input(
    'Задайте направление? (Enc - "Шифрование", Dec - "Дешифрование"): ').lower()
text = input('Введите текст для де/шифрования?: ')


def encryption(step, text):
    result = ''
    for c in text:
        decrypt = ord(c)
        if c.isalpha():
            if c.isupper():
                decrypt = ord(c) + step
                if decrypt > ord(end_upper):
                    decrypt = decrypt - lang_len
            elif c.islower():
                decrypt = ord(c) + step
                if decrypt > ord(end):
                    decrypt = decrypt - lang_len
        result = result + chr(decrypt)
    return result


lst = text.split()
for i in range(len(lst)):
    counter = 0
    # print(len(lst[i]))
    for j in range(0, len(lst[i])):
        # print(lst[i])
        if lst[i][j].isalpha():
            counter += 1
    for k in range(1):
        print(encryption(counter, lst[i]), end=' ')


# def decryption(step, text):
#     result = ''
#     for c in text:
#         decrypt = ord(c)
#         if c.isalpha():
#             if c.isupper():
#                 decrypt = ord(c) - step
#                 if decrypt < ord(start_upper):
#                     decrypt = decrypt + lang_len
#             elif c.islower():
#                 decrypt = ord(c) - step
#                 if decrypt < ord(start):
#                     decrypt = decrypt + lang_len
#         result = result + chr(decrypt)
#     return result


# if de_encryption == 'dec':
#     for i in range(shift_step):
#         print(decryption(i, text))

# if de_encryption == 'enc':
#     for i in range(shift_step):
#         print(encryption(i, text))
