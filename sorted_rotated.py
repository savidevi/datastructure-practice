def find_rotation(l1):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if l1[m]>l1[m+1] and m<n-1:
            return m
        elif l1[h]>l1[m]:
            h=m-1
        else:
            l=m+1
def find_element(l1,val):
    r=find_rotation(l1)
    l=0
    n=len(l1)
    h=n-1
    if val<=l1[r] and val>=l1[l]:
        while l <= r:
            m=(r+l)//2
            if val==l1[m] or m==0:
                return m
            elif val<l1[m]:
                r=m-1
            else:
                l=m+1

    if val>=l1[r+1] and val<=l1[h]:
        while r <= h:
            m = (r + h) // 2
            if val == l1[m] or m == 0:
                return m
            elif val < l1[m]:
                h = m - 1
            else:
                r=m+1

list=[4,5,6,7,1,2,3]
print(find_rotation(list))
print(find_element(list,4))