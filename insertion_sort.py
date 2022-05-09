def insertion_sort(arr):
    for i in range(len(arr)):
        temp=a[i]
        j=i+1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
    return arr
list=[5,4,3,2,7,6,8]
print(insertion_sort(list))