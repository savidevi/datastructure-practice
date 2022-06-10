def maxVal(p,ci,N):
    if (N == 0):
        return 0
    if (ci >= len(p)):
        return 0
    # INCLUDE
    if (p[ci].weight <= N):
        x= maxVal(p, ci+1, N-p[ci].weight) + p[ci].val
    # EXCLUDE
    y = maxVal(p, ci+1, N)
    return max(x, y)
p=[]

def knapsack(weight,value,knw,n):
    if knw==0 or n==0:
        return 0
    if weight[n-1]<=knw:
        x=knapsack(weight,value,knw-weight[n-1],n-1)+value[n-1]
        y=knapsack(weight,value,knw,n-1)
        return max(x,y)
    elif weight[n-1]>knw:
        return knapsack(weight,value,knw,n-1)
weight=[25,50,40,20]
value=[200,350,270,210]
n=len(weight)
knw=100
print(knapsack(weight,value,knw,n))
'''def knapsack(weight,value,knw,n):
    if knw==0 or n==0:
        return 0
    if weight[n-1]<=knw:
        t[m][n]=knapsack(weight,value,knw-weight[n-1],n-1)+value[n-1]
        t[m][n]=knapsack(weight,value,knw,n-1)
        return max(x,y)
    elif weight[n-1]>knw:
        return t[m][n]=knapsack(weight,value,knw,n-1)
weight=[25,50,40,20]
value=[200,350,270,210]
m=len(weight)
n=len(value)
t=[[-1 for i in range(m)]for j in range(n)]
knw=100
print(knapsack(weight,value,knw,n))'''