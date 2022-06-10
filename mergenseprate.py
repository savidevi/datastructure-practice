'''def merge(a,b,n,m):
    i=0
    j=0
    c=[]
    while i<n and j<m:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<n:
        c.append(a[i])
        i+=1
    while j<m:
        c.append(b[j])
        j+=1
    return c


def seprate(a,b,c,n,m):
    a.clear()
    b.clear()
    i=0
    new=len(c)
    while i<n:
        a.append(c[i])
        i+=1
    while i<len(c):
        b.append(c[i])
        i+=1
    return a,b




arr1= [1, 4, 8, 10]

arr2 = [2, 3, 9]
n=len(arr1)
m=len(arr2)
merge(arr1,arr2,n,m)
print(seprate(arr1,arr2,merge(arr1,arr2,n,m),n,m))'''
#MERGE WITHIN
def mergewithin(a,n):
    l=0
    h=n-1
    m=l+h//2


    while l<=m and m<=h:
        if a[m]<a[l]:
            a.append(a[m])

            m+=1

        else:
            a.append(a[l])
            l+=1
    while l<m:
        a.append(a[l])
        l += 1
    while m<h:
        a.append(a[m])

        m += 1

    print(a)
a=[1,3,8,10,2,5,6,9,12,15]

n=len(a)
mergewithin(a,n)