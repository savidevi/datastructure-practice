
str1="ritambhara"
d1={}
for i in str1:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1
print(d1)

d2={}
for i in str1:
    if i in d2:
        d2[i]=d2[i].get(i,0)+1
print(d1)
res = max(d1,key= d1.get)
print(res)
#intersection
a="rijultomar"
b="azruntomar"
c=""
for i in a:
    if i in c or i in b:
        c+=i
print(c)
#union
c=""
for i in a+b:
    if  i not in c:

        c+=i
print(c)
#a-b
c=""
for i in a:
    if i not in b:
        c+=i
print(c)
#b-a
c=""
for i in b:
    if i not in a:
        c+=i

print(c)