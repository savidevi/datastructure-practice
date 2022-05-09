def pascal(n):
    r=1
    while r<n:
        a[0][0] = 1
        a[r][r]=1
        for c in range(r):
            a[r][c]=a[r-1][c-1]+a[r-1][c]
        r+=1
    return a

n=5
a=[[0 for _ in range(n)]for _ in range(n)]

print(pascal(n))