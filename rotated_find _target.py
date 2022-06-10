'''def find(a,n):
    res=0
    for i in a:
        res=res^i
    return res
a=[1,1,2,3,3,4,4,8,8]
n =len(a)
print(find(a,n))

def rotated(a,n):
    l=0
    h=n-1
    while(l<=h):
        m=(l+h)//2
        if m==n-1 or a[m+1]<a[m]:
            return a[m]
        elif a[l]<a[m]:
            l=m+1
        else:
            h=m-1
a=[4,5,6,7,8,9,1,2,3]
n=len(a)
print(rotated(a,n))'''
def rotated_target(arr,n,target):
    low=0
    high=n-1
    while low <= high:
        mid = (low + high)//2
        if (arr[mid] == target):
          return mid
        if (arr[low] <= arr[mid]):
            if (arr[mid] >= target and arr[low] <= target ):
                high = mid - 1
            else:
                low = mid + 1
        elif(arr[mid] <= target and  arr[high] >= target):
            low = mid + 1
        else:
            high = mid - 1

a=[4,5,6,7,8,9,1,2,3]
n=len(a)
print(rotated_target(a,n,1))



