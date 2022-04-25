def negetive_no(a,k):
    s,e=0,0
    i=0
    l=[]
    while e<len(a):
        if a[e]<0:
            l.append(a[e])
        if e-s+1<k:
            e+=1
        elif e-s+1==k:
            if l!=[]:
                print(l[0])
            else:
                print(0)
            if l!=[] and l[0]==a[s]:
                l.pop(0)
            s += 1
            e += 1

arr=[2,3,-1,-3,2,5,6,-7,4,5,-4]
negetive_no(arr,3)