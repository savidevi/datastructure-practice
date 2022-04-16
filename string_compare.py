#def intersection(s1,s2):


str1="ritambhara"
str2="technologies"
str3=[]
print(set(str1)|set(str2))
print(set(str1)&set(str2))

#intersection
for i in str1:
    if i in str2 :
        str3.append(i)
print(str3)
str3.clear()
#union

#str1-str2
for i in str1:
    if i not in str2 :
        str3.append(i)
print(set(str3))
str3.clear()
#str2-str1
for i in str2:
    if i not in str1 :
        str3.append(i)
print(set(str3))