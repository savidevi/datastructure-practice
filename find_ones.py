def first_one(l1):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if m==0 or (l1[m]==1 and l1[m-1]<1):
            return m
        elif l1[m]<1:
            l=m+1
        else:
            h=m-1
def count_one(l1):
    first=first_one(l1)
    h=len(l1)
    if first==-1:
        return -1
    return (h-first)
list=[0,0,0,0,1,1,1,1,1,1,1]
print(first_one(list))
print(count_one(list))