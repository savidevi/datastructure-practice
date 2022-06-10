def kadane(a,n):
    i=0
    j=0
    sum=0
    largest=float("-inf")
    while(j<n):
        sum+=a[j]

        if sum>largest:
            largest=sum
        if sum<0:
            sum=0
        j+=1

    return largest
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n=len(arr)
print(kadane(arr,n))