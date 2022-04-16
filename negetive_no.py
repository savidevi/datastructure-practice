#first nagetive in each list
num=[2,-3,-7,5,-9,4,5,6,9]
s=0
e=0
k=4
a=[]
ans=[]
while e<len(num):
    if num[e]<0:
        a.append(num[e])
    if e-s+1<k:
        e+=1
    elif e-s+1==k:
        if len(a) == 0:
            ans.append(0)
        elif a[0]==num[s]:
            ans.append(a[0])
            a.remove(a[0])
        s+=1
        e+=1
print(ans)

