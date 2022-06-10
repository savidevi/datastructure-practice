'''def mincurr(den,n,ci):
    if n==0:
        return 0
    if den[ci]>n:
        return float("inf")
    if ci>len(den):
        return float("inf")
    x=mincurr(den,n-den[ci],ci+1)+1
    y=mincurr(den,n,ci+1)
    return min(x,y)
den=[1,2,5,10,20,50,100,500]
print(mincurr(den,65,0))'''
def mincurr(dp,den,n,m):
    dp = [[0] *(len(den)+1)for _ in range(n+1)]
    dp[0]=[1]*(len(den)+1)

    for i in range(1,n+1):
        for j in range(1,len(den)-1,-1):
            if (den[i] > n):

                dp[i][j] = dp[i][j+1]

            else:
                dp[i][j] = dp[i][j] + dp[i-den[i]][j]
    print(dp)
    return dp[m][0]
den=[1,2,5,10]
m=len(den)
n=11
dp=[[0 for _ in range(n)]for _ in range(m)]
print(mincurr(dp,den,n,m))

