'''def find(n,num):
    l=1
    h=num
    while l<=h:
        m=l+h//2
        if m

    return ans
print(find(5,243))
print(find(3,27))


def pow(x,n):
    t=1
    if n==0 or x==1:
        return 1
    while n>0:
        t*=x
        n-=1
    return t
print(pow(3,3))
list=[11,33,33,11,33,11]
size=len(list)
d1={}
for i in list:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1
print(d1)
for key,val in d1.items():
    if val >size//3:
        print(key)'''
list=[3,2,4,6]
d1={}
k=6
for i in list:
    if k-i in d1:
        print(i)
    d1[i]=d1









