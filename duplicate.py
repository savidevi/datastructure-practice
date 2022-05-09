
'''nums=[0,0,1,1,1,2,2,3,3,4]
n = len(nums)
k=[set(nums)]
a=[]
i=0
while i<n-1:
    if(nums[i]<nums[i+1]):
        a.append(nums[i])
        i+=1
        if i==n-1:
            a.append(nums[i])
    else:
        i+=1
print(a)
i=0
while i<n-1:
    if nums[i]==nums[i+1]:
        nums.remove(nums[i])
        i-=1
        n=len(nums)
    i+=1
print(n)
print(nums)
'''
'''def duplicates( arr, n):
    j = 1
    a = []
    my_dict = dict()
    for i in arr:
        if i in my_dict:
            t = my_dict.get(i)
            my_dict[i] = t + 1
        else:
            my_dict[i] = j
    for key, value in my_dict.items():
        if value >= 2:
            a.append(key)

    if not a:
        return -1
    else:
        return a
arr=[0 ,3, 1, 2]
print(duplicates(arr,len(arr)))'''
arr=[0,1,1,2,3,2,4]
see=set()
dup=[]
for i in arr:
    if i in see :
        dup.append(i)
    else:
        see.add(i)
if dup==[]:
    print(-1)
else:
    print(dup)


