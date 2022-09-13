
from math import sqrt
for n in range(1, 12):
    for k in range(1, 12):
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                print('n = ', n, 'k = ', k, 'm = ', m)


for b in range(1, 100):
    for k in range(1, 100):
        for t in range(1, 100):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
                print('быков = ', b, 'коров = ', k, 'телят = ', t)


for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                summ = a**5 + b**5 + c**5 + d**5
                e = int(summ**0.2)
                if summ == e**5:
                    print(a + b + c + d + e)
                    break
