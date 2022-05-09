def toh(n,a,b,c):

    if n>0:
        toh(n-1,a,c,b)
        print((a,c),n,end=" ")
        toh(n-1,b,a,c)
toh(3,'1','2','3')