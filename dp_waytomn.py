import numpy as np


def path(m, n):
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return 1
    x = path(m - 1, n)
    y = path(m, n - 1)
    return x + y


print(path(2, 2))


# memorization
def path(m, n):
    if m == 0 and n == 0:
        a[m][n] = 0
    if m == 0 or n == 0:
        a[m][n] = 1
    else:
        a[m][n] = path(m - 1, n) + path(m, n - 1)
    return a[m][n]


a = np.ones((3,3))

print(path(2, 2))
#dp
def path(m, n):

    a[0][0] = 0
    for i in range(m):
        for j in range(n):
            a[i][j] = a[i-1][j] + a[i][j-1]
    return a[m-1][n-1]


a = np.array((3,3))

print(path(2, 2))