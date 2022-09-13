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