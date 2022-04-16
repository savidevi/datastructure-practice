def rotation_point(l1):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if l1[m]>l1[m+1] and m<n-1:
            return l1[m]
        elif l1[h]>l1[m]:
            h=m-1
        else:
            l=m+1
l1=[5,7,8,9,10,1,2,3,4]
print(rotation_point(l1))