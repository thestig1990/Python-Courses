# импорт модуля random
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

quantity_password = int(input('Введите количество паролей для генерации: '))
lenth_password = int(input('Введите длину одного пароля: '))
include_digits = input(
    'Включать ли цифры 0123456789? (Y - "ДА", N - "НЕТ"): ')
include_uppercase_letters = input(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Y - "ДА", N - "НЕТ"): ')
include_lowercase_letters = input(
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Y - "ДА", N - "НЕТ"): ')
include_symbols = input(
    'Включать ли символы !#$%&*+-=?@^_ (Y - "ДА", N - "НЕТ")')
include_othersymbols = input(
    'Исключать ли неоднозначные символы il1Lo0O ? (Y - "ДА", N - "НЕТ"): ')


if include_digits == 'Y' or include_digits == 'Y'.lower():
    chars = chars + digits

if include_uppercase_letters == 'Y' or include_uppercase_letters == 'Y'.lower():
    chars = chars + uppercase_letters

if include_lowercase_letters == 'Y' or include_lowercase_letters == 'Y'.lower():
    chars = chars + lowercase_letters

if include_symbols == 'Y' or include_symbols == 'Y'.lower():
    chars = chars + punctuation

if include_othersymbols == 'Y' or include_othersymbols == 'Y'.lower():
    for c in chars:
        if c in 'iILl1o0O':
            chars = chars.replace(c, '')

print(chars)


def generate_password(lenth_pass, chars):
    password = random.sample(chars, lenth_pass)
    return password


for _ in range(quantity_password):
    print(*generate_password(lenth_password, chars), sep='')
