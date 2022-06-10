def rotate(arr, m, n):
    i = 0
    while i < m:
        for j in range(n):
            rotate_arr[i][j]=arr[n-j-1][i]

        i += 1

    return rotate_arr
arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

m = len(arr)
n = len(arr[0])
rotate_arr=[[0 for _ in range(m)]for _ in range(n) ]
print(rotate(arr, m, n))

def minJumps( arr, n):

    i=0
    count=0
    min=0
    while i<=n-1:
        if i<n-1:
            i+=arr[i]
            count+=1
        if i>=n-1:
            return count
    return -1
arr=[2 ,3 ,1, 1, 2, 4, 2, 0, 1, 1]
print(minJumps(arr,len(arr)))