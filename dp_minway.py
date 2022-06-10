import numpy as np
def minway(a,m,n):
    if m==0 and n==0:
        return a[m][n]
    if m==0 :
        return minway(a,m,n-1)+a[m][n]
    if n==0:
        return minway(a,m-1,n)+a[m][n]
    x=minway(a,m-1,n)
    y=minway(a,m,n-1)
    return min(x,y)+a[m][n]
a=np.array([[2,5,1,2],[1,8,3,1],[9,8,7,2],[5,6,3,4]])
print(minway(a,3,3))
#memorization
def minway(a,m,n):
    if m==0 and n==0:
        return a[m][n]
    if m==0:
        a[m][n]=minway(a,m,n-1)
    if n==0:
        a[m][n]=minway(a,m-1,n)

    a[m][n]=min(minway(a,m-1,n),minway(a,m,n-1))+a[m][n]
    return a[m][n]
a=np.array([[2,5,1,2],[1,8,3,1],[9,8,7,2],[5,6,3,4]])
print(minway(a,3,3))
#dp
def minway(a,m,n):
    a[0][0] = a[0][0]

    for i in range(1,m):
        a[0][i] = a[0][i - 1] + a[0][i]

    for i in range(1,n):
        a[i][0] = a[i - 1][0] + a[i][0]

    for i in range(1,m):
        for j in range(1, n):
            a[i][j] = min(a[i - 1][j], a[i][j - 1]) + a[i][j]

    return a[i][j],a
a=np.array([[2,5,1,2],[1,8,3,1],[9,8,7,2],[5,6,3,4]])
print(minway(a,4,4))

