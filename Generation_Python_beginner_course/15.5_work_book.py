import re

print(ord('А'), ord('Я'), end='\n')
print(ord('а'), ord('я'), end='\n')

print(ord('A'), ord('Z'), end='\n')
print(ord('a'), ord('z'), end='\n')


for i in range(ord('а'), ord('я') + 1):
    print(chr(i), end='')

for i in range(ord('А'), ord('Я') + 1):
    print(chr(i), end='')

print()

for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end='')

for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end='')

print()

for i in range(91, 97):
    print(chr(i), end='')


print()
b = 'Day, mice. "Year" is a mistake!'
s = re.split('[.,?!;:" ]', b)
print(s, len(s))


print()

b = 'Day, mice. "Year" is a mistake!'
s = b.split()
print(s, len(s))
