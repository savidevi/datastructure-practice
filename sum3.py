def subArraySum( arr, n, s):

    i = 0
    k = 0
    l=0
    sum = 0
    while l <=n:

        if sum < s :

            sum += arr[l]
            l +=1
        elif sum>s:
            sum -= arr[i]
            i+=1
        if sum==s:
            return i+1, l
        if l>n:
            return -1
list=[135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]
print(subArraySum(list,42,468))