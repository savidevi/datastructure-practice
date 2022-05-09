def printPat(N,Cap):
    a[0][0] = N
    r = 0
    overflow=False
    if a[0][0] > Cap:
        overflow=True
    while overflow:
        overflow = False
        for c in range(0,r+1):
            if (a[r][c] > Cap):
                temp = a[r][c]-Cap
                a[r][c] = Cap

                a[r+1][c] += temp / 2

                a[r+1][c+1] += temp / 2

                overflow = True
        r+=1
    print(a)
#N is liquid
#cap is glass capacity
Cap=1
N=5

a=[[0 for _ in range(N) ]for _ in range(N)]
printPat(N,Cap)

