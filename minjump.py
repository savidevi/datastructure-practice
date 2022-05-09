'''def minJumps( arr, n):
    jumps = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if (arr[i] == 0):
            jumps[i] = float('inf')
        elif (arr[i] >= n - i - 1):
            jumps[i] = 1
        else:
            # initialize min value
            min = float('inf')

            for j in range(i + 1, n):
                if (j <= arr[i] + i):
                    if (min > jumps[j]):
                        min = jumps[j]
            # Handle overflow
            if (min != float('inf')):
                jumps[i] = min + 1
            else:
                # or INT_MAX
                jumps[i] = min

    return jumps[0]
'''


def minJumps(arr, l, h):
    if (h == l):
        return 0
    if (arr[l] == 0):
        return float('inf')
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and jumps + 1 < min):
                min = jumps + 1
    return min
def fun(arr,n):
    return minJumps(arr,0,n-1)

arr =[3,2,1]
n=len(arr)

print(fun(arr,n-1))