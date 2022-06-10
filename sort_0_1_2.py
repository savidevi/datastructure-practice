'''def sort0(arr,n):
    for i in range(0,n):
        for j in range(n-1,0,-1):
            if i > j:
                break
            if arr[i] <= arr[j]:
                continue
            if arr[i]>arr[j] and i<j:
                arr[i],arr[j]=arr[j],arr[i]

    print(arr)

arr=[1,2,2,0,2,0,1,2,0,1,1]
sort0(arr,len(arr))'''
def sort1(arr,n):
    l=0
    h=n-1
    m=0
    while m<=h:
        if arr[m] ==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        if arr[m]==1:
            m+=1
        if arr[m]==2:
            arr[h], arr[m] = arr[m], arr[h]
            h-=1
    print(arr)
arr=[1,2,2,0,2,0,1,2,0,1,1]
sort1(arr,len(arr))





