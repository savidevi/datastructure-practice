def first_occur(l1,val):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if  m==0 or (val==l1[m] and val>l1[m-1]) :
            return m
        elif l1[m]>=val:
            h=m-1
        else:
            l=m+1

def last_occ(l1,val):
    l=0
    n=len(l1)
    h=n-1
    while l<=h :
        m=(l+h)//2
        if  m==h or (l1[m]==val and val<l1[m+1]) :
            return m
        if l1[m]>val:
            h=m-1
        else:
            l=m+1

def count_occur(l1,val):
    l=first_occur(l1,val)
    h=last_occ(l1,val)

    if l==0:
        return -1
    return (h-l)+1

list=[3,3,3,4,4,5,5,6,6,6,7,8,8]
print(first_occur(list,2))
print(last_occ(list,2))
print(count_occur(list,2))
