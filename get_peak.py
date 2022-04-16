def peak(l1):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if l1[m]>l1[m-1] and l1[m]>l1[m+1]:
            return l1[m]
        elif l1[m]<l1[m-1]:
            h=m-1
        else:
            l=m+1
list=[1,8,6,3,7,10,8,9,2]
print(peak(list))