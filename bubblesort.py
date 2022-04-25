def bubble_sort(arr):
    n=len(arr)
    i=0
    while(n>1):
        i=0
        while i<n-1:

            if arr[i]>arr[i+1]:
                swap(arr,i+1,i)

            i+=1
        n-=1
    return arr
def swap(arr,i,j):
    arr[j]=arr[i]+arr[j]
    arr[i]=arr[j]-arr[i]
    arr[j]=arr[j]-arr[i]
    return arr,i,j
list=[2,4,7,6,3,1]
print(bubble_sort(list))

