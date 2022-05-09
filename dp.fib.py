def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(7))
def fib1(a,n):
    a.insert(0,1)
    a.insert(1,1)

    for i in range(2,n):
        r=a[i-1]+a[i-2]
        a.insert(i,r)
    return r
a=[]
print(fib1(a,7))
