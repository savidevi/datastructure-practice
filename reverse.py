n = 0
t =0
x=-0

p=0
if x<0:
    p=x
    x=-x
if x>=x**31 or x<=(-x**31-1 ) :
            print("0")

while x > 0:
    n = x % 10

    t = (t*10)+n

    x = x // 10
if(p<0):
   print("-",+t)
else:
    print(t)


