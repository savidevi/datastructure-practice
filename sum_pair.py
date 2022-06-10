def countKdivPairs(self, arr, n, k):
    # code here
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count


def countKdivPairs( l, n, k):
    freq = {}
    ct = 0
    for i in l:
        md = i % k
        if md != 0:
            if k - md in freq:
                ct += freq[k - md]
        else:
            if md in freq:
                ct += freq[md]

        if md in freq:
            freq[md] += 1
        else:
            freq[md] = 1

    return ct
l=[2, 2, 1, 7, 5, 3]
n=len(l)
print(countKdivPairs(l,n,4))


def merge( nums1, nums2,m, n):
    i = 0
    j = 0
    nums = []
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    while i < m:
        nums.append(nums1[i])
        i += 1
    while j < n:
        nums.append(nums2[j])
        j += 1
    return nums
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
print(merge(nums1,nums2,m,n))