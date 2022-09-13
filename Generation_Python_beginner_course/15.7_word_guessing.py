import random
word_list = []
# открыываем файл "word_rus.txt", считываем его построчно и добавляем строки в список "word_list"
with open('word_rus.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word_list.append(line.strip())
# print(len(word_list))


# ф-ция для выбора случайного слова из списка "word_list"
def get_word(list):
    word = random.choice(list).upper()
    return word


# print(get_word(word_list))


# ф-ия display_hangman() принимает один аргумент tries – количество попыток угадывания слова и
# возвращает текущее состояние игры в графическом виде
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
    - - - - - - - -
    |             |
    |             O
    |            \\|/
    |             |
    |            / \\
    -
    ''',
        # голова, торс, обе руки, одна нога
        '''
    - - - - - - - -
    |             |
    |             O
    |            \\|/
    |             |
    |            /
    -
    ''',
        # голова, торс, обе руки
        '''
    - - - - - - - -
    |             |
    |             O
    |            \\|/
    |             |
    |
    -
    ''',
        # голова, торс и одна рука
        '''
    - - - - - - - -
    |             |
    |             O
    |            \\|
    |             |
    |
    -
    ''',
        # голова и торс
        '''
    - - - - - - - -
    |             |
    |             O
    |             |
    |             |
    |
    -
    ''',
        # голова
        '''
    - - - - - - - -
    |             |
    |             O
    |
    |
    |
    -
    ''',
        # начальное состояние
        '''
    - - - - - - - -
    |             |
    |
    |
    |
    |
    -
    '''
    ]
    return stages[tries]


# ф-ция определяющая логику игры
def play(word):
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '?' * len(word)
    guessed = False                     # сигнальная метка
    guessed_letters = []                # список уже названных букв
    guessed_words = []                  # список уже названных слов
    tries = 6                           # количество попыток
    print('Давайте начнем нашу викторину по угадыванию слов!')
    print('Текущее состояние игры: ', display_hangman(tries))
    print('Количество попыток: ', tries)
    print('Слово: ', word_completion)
    while not guessed and tries > 0:
        letter = input('Угадайте букву или слово целиком: ').upper()
        letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
        if len(letter) == 1 and letter in letters:
            if letter in guessed_letters:
                print(f'Вы уже называли букву: {letter}')
            elif letter not in word:
                print(f'Буквы {letter} нет в слове.')
                tries -= 1
                guessed_letters.append(letter)
            elif letter in word:
                print(
                    f'Поздравляем! Вы угадали! Буква {letter} присутствует в слове')
                guessed_letters.append(letter)
                for i in range(len(word)):
                    if letter == word[i]:
                        word_completion = word_completion[:i] + \
                            letter + word_completion[i+1:]
                if '?' not in word_completion:
                    guessed = True
        elif len(letter) == len(word) and letter.isalpha():
            if letter in guessed_words:
                print(f'Вы уже называли слово: {letter}')
            elif letter != word:
                print(f'Слово {letter} не верное!')
                tries -= 1
                guessed_words.append(letter)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово: ')
        print(display_hangman(tries))
        print(word_completion)
        print()

    if guessed:
        print('Примите наши поздравления! Вы угадали слово целиком!')
    else:
        print(
            f'Вы не смогли угадать слово {word}. В следующий раз у Вас всё получится!')


# основной цикл программы

play_or_no = 'ДА'

while play_or_no == 'ДА':
    play(get_word(word_list))
    play_or_no = input('Рискнёте сыграть ещё раз? (да или нет): ').upper()
