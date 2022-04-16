
nums=[3,2,2,3]
k = 0
val=3
n = len(nums)
for i in range(n):
    if nums[i] != val:
        nums[k] = nums[i]

        k += 1


print(k)
print(nums)