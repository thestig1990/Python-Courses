numbers = list(range(1, 10, 2))
for i in numbers:
    print(i, end='*')


# print(list(range(2, int(input()) + 1, 2)))
print()
chars = [c for c in 'abcdefg']
print(chars)

# print(input().split() for _ in range(int(input()))


# print(len(max(input().split())))

#print(max([len(i) for i in input().split()]))


# z = input().split()
# for i in range(len(z)):
#     z[i] = z[i][1:] + z[i][0] + 'ки'
#     print(z[i], end=' ')


#print([i][1:] + [i][0] + 'ки' for i in range(len(input().split())))

s = input().split('-')
# # print(s)
# print(''.join(s).isdigit())
if ''.join(s).isdigit():
    if s[0] == '7':
        del s[0]
    print(s)
    if len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# s = ['7', '301', '447', '5820']
# del s[0]
# print(s)
