weight=[30,30,40,15]
value=[270,240,280,150]
rate_per_kg=[]
n=len(weight)
totalvalue=0

knapsack=100
for a in range(len(weight)):
    rate_per_kg.append(value[a]//weight[a])

print(max(rate_per_kg))

for i in range(n):
    for j in range(n):
        if max(rate_per_kg)==rate_per_kg[j]:
            knapsack-=weight[j]
            print(knapsack)
            rate_per_kg[j]=0
            if knapsack>0:
                totalvalue+=value[j]
            else:
                break

print( totalvalue)


def knapsack_prob(weight,value,knapsack,n):
    if knapsack==0 or n==0:
        return 0
    if weight[n-1]<=knapsack:
        x=knapsack_prob(weight,value,knapsack-weight[n-1],n-1)+value[n-1]
        y=knapsack_prob(weight,value,knapsack,n-1)
        return max(x,y)
    elif weight[n-1]>knapsack:
        return knapsack_prob(weight,value,knapsack,n-1)

weight=[30,30,40,15]
value=[270,240,280,150]

n=len(weight)

knapsack=100
print(knapsack_prob(weight,value,knapsack,n))


def maxCoins( A, B, T, N):
    if T == 0 or N == 0:
        return 0
    if A[N - 1] <= T:
        x = maxCoins( A, B, T - A[N - 1], N - 1) + B[N - 1]
        y = maxCoins( A, B, T, N - 1)
        return max(x, y)
    else:
        return maxCoins(A, B, T, N - 1)
T = 3
N = 3
A=[1, 2, 3]
B=[3, 2, 1]


print("max coin:",maxCoins(A,B,T,N))


# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result
def subArraySum(arr, n, sum_):
    # Pick a starting
    # point
    for i in range(n):
        curr_sum = arr[i]

        # try all subarrays
        # starting with 'i'
        j = i + 1
        while j <= n:

            if curr_sum == sum_:
                print("Sum found between")
                print("indexes % d and % d" % (i, j - 1))

                return 1

            if curr_sum > sum_ or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print("No subarray found")
    return 0


# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 33

subArraySum(arr, n, sum_)


def duplicates( arr, n):
    arr.sort()
    duplicate = set()
    a = set()
    for i in arr:
        if i in duplicate :
            a.add(i)
        else:
            duplicate.add(i)
    if a == []:
        return -1
    else:
        return a
arr=[13 ,9, 25, 1, 1, 0, 22, 13, 22, 20, 3 ,8 ,11 ,25, 10, 3 ,15, 11, 19, 20, 2 ,4 ,25, 14 ,23 ,14]
n=26
print(duplicates(arr,n))