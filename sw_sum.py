'''def sum(arr,n,s):
    i = 0
    k = 0
    j = 0
    sum = 0
    while j < n:
        sum += arr[j]
        if sum < s:
            j += 1
        elif sum > s:
            while sum > s:
                sum-=arr[i]
                i += 1
            j+=1
        if sum == s:
            return i + 1, j
arr=[1,2 ,3, 4, 5, 6, 7, 8, 9, 10]
print(sum(arr,len(arr),15))


def countDistinct(arr, n, k):
    i = 0
    j = 0
    max = arr[0]
    a = []
    d = []
    while j < n:
        a.append(arr[j])
        if j - i + 1 < k:
            j += 1
        elif j-i+1 == k:
            for m in a:
                if m > max:
                    max = m
            d.append(max)
            a.remove(a[0])
            i += 1
            j += 1
    return d
arr=[ ]
n=len(arr)
print(n)
print(countDistinct(arr,n,))'''

def loop(a,h):
    for i in a:
        if h==i:
            print("found")
            return
a=[1,2,3,4,5,6,7,8]
h=5
loop(a,h)