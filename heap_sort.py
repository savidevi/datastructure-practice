def heapify(a, r, n):
    if (r >=n):
        return
    min = r
    left=(2 * r) + 1
    right=(2 * r) + 2
    if left < n and (a[min] > a[left]):
        min = left
    if right< n and ( a[min] > a[right]):
        min = right
    if (min != r):
        swap(a, r, min)
        heapify(a, min,n)

def insert(a,n, val):
    a.append(val)
    while n>0 and (a[(n-1)//2] >a[n]):
        swap(a, n, (n-1)//2)
        n = (n-1)//2


def remove( a, n):
    a.pop(0)
    heapify(a, 0, n)
    return
def swap(a,i,j):
    a[j]=a[i]+a[j]
    a[i]=a[j]-a[i]
    a[j]=a[j]-a[i]
def sort():



def heapsort():


list=[3,5,1,7,8,13,9,12,16,19]
n=len(list)
r=0
heapify(list, r, n)
print(list)
insert(list,n, 2 )

print(list)
heapify(list,r,n)
print(list)
remove( list, n)
print(list)