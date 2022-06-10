def search(matrix,m,n,s):
    l=0
    h=(m*n)-1
    while l<h:
        mid=l+h//2
        if matrix[mid//m][mid % m]==s:
            return True
        if matrix[mid//m][mid%m]<s:
            l=mid+1
        else:
            h=m-1

    return False
matrix=[[1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]]
n=len(matrix)
m=len(matrix[0])
print(search(matrix,m,n,12))