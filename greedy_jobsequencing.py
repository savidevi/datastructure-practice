def max_profit(arr,n,t):
     for i in range(n):
          for j in range(n-1-i):
               if arr[j][2]<arr[j+1][2]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
     print(arr)
     result=[False]*t
     job=['-1']*t
     for i in range(n):
          for j in range(min(t-1,arr[i][1]-1),-1,-1):
               if result[j]==False:
                    result[j]=True
                    job[j]=arr[i][0]
                    break
     print(job)
arr=[['a1',3,10],
     ['a2',4,5],
     ['a3',3,15],
     ['a4',3,25],
     ['a5',1,2],
     ['a6',3,12]]
max_profit(arr,len(arr),5)

