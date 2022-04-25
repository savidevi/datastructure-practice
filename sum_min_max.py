def max_sum(a,k):
    n=len(a)
    s,l,max,sum=0,0,0,0
    while l<n:
        sum+=a[l]
        if l-s+1<k:
            l+=1
        elif l-s+1==k:
            if sum > max:
                max = sum
            sum-=a[s]
            s+=1
            l+=1
    return max
def min_sum(a,k):
    n=len(a)
    s,e,min,sum=0,0,10,0
    while e<n:
        sum+=a[e]
        if e-s+1<k:
            e+=1
        elif e-s+1==k:

            if sum<min:
                min=sum
            sum-=a[s]
            s+=1
            e+=1
    return min

arr=[1,2,1,3,5,1,3,0,0,2,3,4]
print(min_sum(arr,3))