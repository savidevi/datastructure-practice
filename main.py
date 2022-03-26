'''class solution:
    def missingNumber(self, array,n):
        x=[]
        for i in range(1,n+1):
            x.append(i)

        print(x)
        p= sum(x)-sum(array)
        print(p)



s1 = solution()
li=[1,2,4,5]
t=5
s1.missingNumber(li,t)'''
arr=[1,2,3,7,5]
#print(sum(arr))
j = 1
x=[]
i=0
for i in range(6):
    for number in arr[i:]:
        j+=1
        x.append(number)
        if sum(x)>12:
            #print(x,i,j)
            x.clear()
            break
        elif sum(x)==12:
            print(x,i+1,j)

    j=1
    i+=1





