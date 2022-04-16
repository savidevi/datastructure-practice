#without repeated character
str='eabebrtsmk'
a=[]
s=0
e=0
maxcnt=0
cnt=0
while(e<len(str)):
    if str[e] not in a:
        a.append(str[e])
    if len(a)==e-s+1:
        e+=1
        cnt=len(a)
        if cnt>maxcnt:
            maxcnt=cnt
    else:
        a.remove(a[0])
        s+=1
        e+=1

print(maxcnt)