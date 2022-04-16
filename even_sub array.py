a=[1,3,3,3,7,3,3,3,6,3,7,6,7,9,3,5]
maxcnt=0
cnt=0
n=len(a)
s=0
e=0
k=4
while e<n:
    if a[e]%2==0 :
        cnt+=1
    if e-s+1<k:
        e+=1
    elif e-s+1==k:
        if cnt>maxcnt:
            maxcnt=cnt
        if a[s]%2==0:
            cnt-=1
        s += 1
        e += 1

print(maxcnt)








