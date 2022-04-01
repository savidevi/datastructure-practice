
nums=[0,0,1,1,1,2,2,3,3,4]
n = len(nums)
'''k=[set(nums)]
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
print(a)'''
i=0
while i<n-1:
    if nums[i]==nums[i+1]:
        nums.remove(nums[i])
        i-=1
        n=len(nums)
    i+=1
print(n)
print(nums)