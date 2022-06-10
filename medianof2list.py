'''def merge(a,b,m,n):
    i,j=0,0
    c=[]
    while i<m and j<n:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<m:
        c.append(a[i])
        i+=1
    while j<n:
        c.append(b[j])
        j+=1
    print(c)
    lenc=len(c)
    if lenc%2==0:
        median= lenc//2
    else:
        median= (lenc+1)//2
    return c[median-1]

a=[1]
b=[2]
m=len(a)
n=len(b)
print(merge(a,b,m,n))'''
def merge(a,b,m,n,k):
    i,j=0,0
    c=[]
    while i<m and j<n:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<m:
        c.append(a[i])
        i+=1
    while j<n:
        c.append(b[j])
        j+=1
    print(c)
    return c[k-1]

a=[]
b=[1,4,8,10]
m=len(a)
n=len(b)
print(merge(a,b,m,n,2))