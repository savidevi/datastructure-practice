
def ones(arr,i,j):
    while j <= 4:
        for i in range(0, 4):
            if arr[i][j] == 1:
                return i
            elif i==3 and j==3:
                return -1
        else:
            j += 1
            i += 1
    if i==4 and j==4:
        return -1
arr=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
i=0
j=0
print(ones(arr,i,j))


