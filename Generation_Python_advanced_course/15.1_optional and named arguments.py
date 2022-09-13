# Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу
# заданного размера. При этом (в зависимости от переданных аргументов) она
# должна вести себя так:

# matrix() — возвращает матрицу 1×1, в которой единственное число равно нулю;
# matrix(n) — возвращает матрицу n×n, заполненную нулями;
# matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями
# matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой
# каждый элемент равен числу value.

# VAR1
def matrix(n=1, m=None, value=None):
    if m is None:
        m = n
    if value is None:
        matrix1 = [[0]*m for _ in range(n)]
    else:
        matrix1 = [[value]*m for _ in range(n)]
    return matrix1


print(matrix(3, 1))


# VAR2
def matrix_new(n=1, m=None, value=0):
    if m is None:
        m = n
    matrix1 = [[value]*m for _ in range(n)]
    return matrix1


print(matrix_new(3, 1))
