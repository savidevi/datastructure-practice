def noOfWays(m,n):
    if m==0 and n==0:
        return 0
    if m==1 or n==1:
        return 1
    x=noOfWays(m,n-1)
    y=noOfWays(m-1,n)
    return x+y
print(noOfWays(4,4))
'''def noofways(m,n):
    a=[[0 for i in range(m)]for j in range(n)]
    for i in range (m):
        a[i][0]=1
    for j in range(n):
        a[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            a[i][j] =a[i-1][j]+a[i][j-1]
    return a[m-1][n-1]

print(noofways(4,4))
def print_path(m,n):
    if m==0 and n==0:
        return
    if m !=0 and n !=0:
        print(m - 1, n - 1, end=" ")
        print_path(m,n-1)
        print_path(m-1,n)

print_path(4,4)
def print_path_dp(m,n):
    a=[[0 for i in range(m)]for j in range(n)]
    if m!=0 and n!=0:
        
        for i in range(m):
            for j in range(n):
                print(i,j)
print_path_dp(3,3)'''

