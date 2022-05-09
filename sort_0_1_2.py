def sort0(arr,n):
    for i in range(0,n):
        for j in range(n-1,0,-1):
            if i > j:
                break
            if arr[i] <= arr[j]:
                continue
            if arr[i]>arr[j] and i<j:
                arr[i],arr[j]=arr[j],arr[i]

    print(arr)

arr=[1,2,2,0,0,0,1,2,0,1,1]
sort0(arr,len(arr))
