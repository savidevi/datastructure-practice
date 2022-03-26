'''def roman(s):
    a = 0
    rn = s
    i = 1
    for i in range(len(s)):
        if rn[i] == 'M':
            a += 1000
        elif rn[i] == 'D':
            a += 500
        elif rn[i] == 'C':
            a += 100
        elif rn[i] == 'L':
            a += 50
        elif rn[i] == 'X':
            a += 10
        elif rn[i] == 'V':
            a += 5

        elif rn[i] == 'I':
            a += 1
        if i>0:
            if rn[i] == 'V' and rn[i - 1] == 'I':
                a -= 2
            if rn[i] == 'X' and rn[i - 1] == 'I':
                a -= 2
            if rn[i] == 'L' and rn[i - 1] == 'X':
                a -= 20
            if rn[i] == 'C' and rn[i - 1] == 'X':
                a -= 20
            if rn[i] == 'D' and rn[i - 1] == 'C':
                a -= 200
            if rn[i] == 'M' and rn[i - 1] == 'C':
                a -= 200

    print(a)
roman('MMMCDXC')'''

'''n=3

a=[]
t=1000
b=0
s=[]
cnt=0

while n>0 and cnt<=4:

    a.append(n//t)
    n=n%t
    t=int(t/10)
    if n==0 and t>=1 :
        a.append(0)
        n=1

    cnt+=1

print(a)
#for i in range(len(a)):
if a[0]>0:
    for j in range(a[0]):
        s.append('M')

if a[1]>0:
    if a[1] >= 5 and a[1] < 9:
        b = a[1] - 5
        s.append('D')
        for j in range(b):
            s.append('C')
    elif a[1] == 4:
        s.append('CD')
    elif a[1] == 9:
        s.append('CM')
    else:
        for j in range(a[1]):
            s.append('C')
if a[2]==0:
    print()
if a[2]>0:
    if a[2] >= 5 and a[2] < 9:
        b = a[2] - 5
        s.append('L')
        for j in range(b):
            s.append('X')

    elif a[2] == 4:
        s.append('XL')
    elif a[2] == 9:
        s.append('XC')
    else:
        for j in range(a[2]):
            s.append('C')
if a[3]==0:
    print()
if a[3]>0:
    if a[3] >= 5 and a[3] < 9:
        b = a[3] - 5
        s.append('V')
        for j in range(b):
            s.append('I')
    elif a[3] == 4:
        s.append('IV')
    elif a[3] == 9:
        s.append('IX')
    else:
        for j in range(a[3]):
            s.append('I')

print(s)
str=""
st=str.join(s)
print(st)'''

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                num+=roman[s[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman[s[i]]
                i+=1
        return num

ob1 = Solution()
print(ob1.romanToInt("III"))
print(ob1.romanToInt("MDXLIII"))'''


# Python3 program to convert
# integer value to roman values

# Function to convert integer to Roman values
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:

        div = number // num[i]

        number %= num[i]
        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


# Driver code
if __name__ == "__main__":
    number = 3
    print("Roman value is:", end=" ")
    printRoman(number)
