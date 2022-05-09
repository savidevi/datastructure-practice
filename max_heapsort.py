
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
def find_kth_largest(arr) :
    for i in range(0,k+1):
        heapify(arr,n,i)
        if arr[t]>arr[0]:
            kth=arr[t]
    return arr[t]

arr = [5,7,4,69,83,12,3,1]
n = len(arr)
heapify(arr,n,0)
print(arr)
heapSort(arr)

print(arr)


