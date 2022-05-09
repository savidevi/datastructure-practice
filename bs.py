
'''def search(l1,k):
    n=len(l1)
    l=0
    h=n-1
    while l<=h:
        m =(l+h) //2
        if(l1[m]==k):
            return True
        elif l1[m]>k:
            h=m-1
        else:
            l=m+1
    return False
def insert_no(l1,val):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if (val<l1[m] and val>l1[m-1]) :
            l1.insert(m-1,val)
            return l1
        elif (val>l1[m] and val<l1[m+1])or val==l1[m] :
            l1.insert(m+1,val)
            return l1
        elif val>l1[n-1]:
            l1.append(val)
            return l1
        elif l1[m]>val:
            h=m-1
        else:
            l=m+1


def remove_no(l1,val):
    l=0
    n=len(l1)
    h=n-1
    while l<=h:
        m=(l+h)//2
        if l1[m]==val:
            l1.remove(val)
            return l1
        elif l1[m]>val:
            h=m-1
        else:
            l=m+1'''


def peakElement( arr, n):

    l = 0
    h = n - 1
    while l < h:
        m = l + (h - l) // 2

        if arr[m + 1] > arr[m]:
            l = m + 1
        else:
            h=m

    return l

list = [4,5,6,7,8,9,0,1]
print(peakElement(list,len(list)))
#print(search(list,11))
#print(insert_no(list,144))
#print(remove_no(list,100))