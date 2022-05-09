'''A=[[1 ,1 ,1 ,0],
[1, 1, 0, 0],
[0, 0, 1, 1],
[1 ,1 ,1 ,1]]
r=0
c=0
N=len(A)
M=len(A[0])
count=0
x=1
min=float('inf')
while r<M and c<N:
    for i in range(c,M):
        if A[r][i]==1:
            count+=1
    if min>count:
        min=count
        x+=r
    r+=1
    count=0
if min==0 :
    print(x)
else:
    print(x)'''

def antidia(A,n):
    def printline(i, j, row):
        while i<n and j >=0:
            row.append(A[i][j])
            i += 1
            j -= 1


    row = []
    for i in range(0, n):
        printline(0, i, row)
    for j in range(1, n):
        printline(j,n-1, row)
    return row
A=[[1, 2],
    [3,4]]
n=len(A)
print(antidia(A,n))
