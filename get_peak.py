def peak(l1):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=l+(h-l)//2
        if m==h or l1[m]>l1[m-1] and l1[m]>l1[m+1]:
            return l1[m]
        elif l1[m]<l1[m-1]:
            h=m-1
        else:
            l=m+1
list=[1,2,3]
print(peak(list))