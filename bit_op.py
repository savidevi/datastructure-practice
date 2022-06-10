
def find_unique(list):
    res=0
    for i in range(len(list)):
        res =res^list[i]
    return "odd unique={}".format(res)
list=[5,5,5,4,3,2,3,2,6,6,4]
print(find_unique(list))
# find missing no in consecutive numbers
def missing_no(a,n):
    res = 0
    #res1 = 1
    for i in a:
        res = res ^ i
    for i in range(1, n+2):
        res = res ^ i
    return "missing no:{}".format(res)
a=[1,4,8,9,5,6,3,2]
n=len(a)
print(missing_no(a,n))
#repetitive no
def repeated_no(arr,n):
    res = 0
    # res1=1
    for i in arr:
        res = res ^ i
    for i in range(1, n):
        res = res ^ i
    return "repeated no :{}".format(res)
a=[1,4,8,7,5,6,3,2,4]
n=len(a)
print(repeated_no(a,n))

def missing_repeated(a,n):
    res=0
    for i in a:
        res=res^i
    for i in range(1,n):
        res=res^i
    set_bit=res & ~(res-1)
    x=0
    y=0
    for i in range(1,n):
        if set_bit==0:
            x=x^res
        if set_bit==1:
            y=y^res
    for i in range(1, n ):
        if i & set_bit:
            x = x ^ i
        else:
            y = y ^ i

    return "Two  Numbers are %d %d" % (x, y)
a=[1,2,3,3,4]
print(missing_repeated(a,len(a)))

def find_power(x,n):
    ans = 1

     while (n > 0):
        last_bit = (n & 1)
        if last_bit==1:
            ans = ans * x
        x = x * x
        n = n >> 1 #right shift

    return ans
print(find_power(2,2))
def powerof_2(x):
    #for x in range(2,21,2):

    if (x & (x-1))==0:
        return True
    return False

print(powerof_2(6))'''