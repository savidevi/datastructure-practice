'''a=[3,1,4,4,2]
res=0
n=len(a)
for i in a:
    res=res^i
for i in range(n):
    res=res^i
print(res)'''


# Python3 code to Find the repeating
# and the missing elements

def printTwoElements(arr, size):
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print("The repeating element is ", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("and the missing element is ", i + 1)



arr = [8, 3, 4, 5, 5, 6, 2,1]
n = len(arr)
printTwoElements(arr, n)

