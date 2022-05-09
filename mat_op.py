import matrix1 as m




'''def diagonal():
    for i in range(len(m.a)):
        print(m.a[i][i],end=" ")

def printline(i,j):

    while i>=0 and j<n:
        print(m.a[i][j],i,j)
        i-=1
        j+=1
n=len(m.a)
for i in range(0,n):
    printline(i,0)
for j in range(1,n):
    printline(n-1,j)

def spiral():

    n=len(m.a)
    sr,sc=0,0
    er,ec=len(m.a),len(m.a[0])

    print(len(m.a),len(m.a[0]))
    while sr<er and sc<ec:
        for i in range(sc,ec):
            print(m.a[sr][i],end=" ")
        for i in range(sr+1,er):
            print(m.a[i][ec-1] ,end=" ")
        if sr!=er:
            for i in range(ec-2,sc-1,-1):
                print(m.a[er-1][i], end=" ")
        if sc!=ec:
            for i in range(er-2,sr,-1):
                print(m.a[i][sc],end=",")
        sr+=1
        sc+=1
        er-=1
        ec-=1
spiral()'''

#Function to search a given number in row-column sorted matrix.
def search(self,matrix, n, m, x):
    r = 0
    c = m-1
    while r < n and c>=0:
        if matrix[r][c] == x :
            return 1
        elif matrix[r][c]>x:
            c-=1
        else:
            r+=1

    return 0


matrix=[[ 3, 30, 38],
        [36, 43, 60],
         [40, 51, 69]]
m = len(matrix)
n = len(matrix[0])
print(search(matrix,n,m,69))
