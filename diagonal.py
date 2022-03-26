matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
#for diagonal print
'''for i in range(len(matrix)):
    print(matrix[i][i])'''
#for diagonal print THIRD rows

n=len(matrix)
#print(n)
'''for i in range(n):
    print(matrix[n-1][i])
    n=n-1'''
#spiral
'''i=0
j=0
for j in range(n):
    print(matrix[i][j])
for i in range(n-1):
    print(matrix[i+1][j])
for j in reversed(range(j)):
    print(matrix[i+1][j])
for i in reversed(range(n-1)):
    if i==0:
        break
    print(matrix[i][j])
i+=1
for j in range(n-2):
    print(matrix[i][j+1])
for j in reversed(range(n-1)):
    if j==0:
        break
    print(matrix[i+1][j])'''
#diagnol all element
for i in  range(n):
    for j in range(i+1):
        print(matrix[i][j],end=(","))
        i-=1
j=0
for k in range(n):
    i=n-1
    for j in range(n):
        if(i>=1 and j>=k+1):
            print(matrix[i][j],end=(","))
            i-=1






















