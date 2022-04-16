a=[1,2,20,1,5,3,1,8,10]
k=4
sum=0
e=0
s=0
maxsum=sum

while e<len(a):
    sum+=a[e]
    if e-s+1<k:
        e+=1
    elif e-s+1==k:
        if sum > maxsum:
            maxsum = sum
        sum=sum-a[s]
        s+=1
        e+=1

print(maxsum)

