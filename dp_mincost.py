def mincost(n):
    if n==0 or n==1:
        return a[0][1]
    mc=a[0][n]
    for i in range(n):
        temp=mincost(i)+a[i][n]
        if temp<mc:
            mc=temp
    return mc
a=[[0,10,40,80],[0,0,25,45],[0,0,0,35],[0,0,0,0]]
print(mincost(3))
 