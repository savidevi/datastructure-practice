'''st="StriNG"
st1=""
for i in st:
    if i.isupper():
        i=i.lower()
        st1+=i
    else:
        i=i.upper()
        st1+=i
print(st1 )

vowels="aeiou"
st="eiouawrpoi"
count=0
for i in st:
    if i in vowels:
        count+=1

print(count)


str="civics"
rev=str[::-1]
print(rev)
if str==rev:
    print("p")
else:
    print("not p")

st="12rt3"
sum=0
temp="0"
for i in st:
    if i.isdigit():
        temp+=i
    else:
        sum+=int(temp)
        temp="0"
print(sum+int(temp))


st="aabra ka dabra"
print(st.count('a'))


str="dollar"
st="cod"
str=str.replace('ll','dd')
print(str)

str=" aabra ka dabara "
str="".join(str.split())
print(str)


def ispar( x):

    brackets = "({["
    brackets1 = ")}]"

    y = []
    for i in x:
        if i in brackets:
            y.append(i)
        elif i in brackets1:
            ind=brackets1.index(i)
            if y!=[] and brackets[ind]==y[len(y)-1]:
                y.pop()
            else:
                return False
    if y == []:
        return True

str="{([])}"
print(ispar(str))


def isValid(s):
    print(s.split("."))
    if len(s.split(".")) < 4 or len(s.split(".")) > 4:
        return 0
    for i in s.split("."):
        print
        if i=="" or i[0]=='0':
            return 0

    for i in s.split("."):
        if i =="":
            return 0
        if i.isdigit() and (int(i) < 255 and int(i) >=0) and i.count('0') < 2:
                continue
        else:
            return 0
    return 1
str="172.16.254.100"
print(isValid(str))'''


def strstr(s,x):
    #code here
    k=len(x)
    t=""
    i=0
    j=0
    n=len(s)
    while(j<n):
        t+=(s[j])
        if (j-i)+1<k:
            j+=1
        elif (j-i)+1 ==k:
            if t==x:
                return i
            t=t[1:]
            i+=1
            j+=1
    return -1
print(strstr("geeksforgeeks","for"))


def isAnagram( a, b):
    if sorted(a.lower()) == sorted(b.lower()):
        return "Yes"
    else:
        return "No"
a="b"
b="d"
print(isAnagram(a,b))