def find_zero(mat,m,n):
    i=0
    while i<m:
        for j in range(n):
            if mat[i][j]==0:
                row=i
                column=j
                return row ,column

        i+=1
def set_matrix_zero(row,column) :        
    for i in range(n):
        mat[row][i]=0
        mat[i][column]=0
    return mat


mat=[[1,0,3,4],
     [5,6,7,12],
     [8,9,10,11],
     [12,13,14,0]]
m=len(mat)
n=len(mat[0])
row,column=find_zero(mat,m,n)
print(set_matrix_zero(row,column))
