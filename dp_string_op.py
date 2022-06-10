'''def subsequence(s1,s2,i,j):
    if i<0 or j<0:
        return 0

    if s1[i-1]==s2[j-1]:
        return subsequence(s1,s2,i-1,j-1)+1
    else:
        return max(subsequence(s1,s2,i-1,j),subsequence(s1,s2,i,j-1))
s1=['a','b','a','c','x','g']
s2=['b','a','x','p']
print(subsequence(s1,s2,len(s1),len(s2)))

def subsequence(s1,s2,i,j):
    if i==len(s1) or j==len(s2):
        return 0

    if s1[i]==s2[j]:
        return subsequence(s1,s2,i+1,j+1)+1
    else:
        return max(subsequence(s1,s2,i+1,j),subsequence(s1,s2,i,j+1))
s1=['a','b','a','c','x','g']
s2=['b','a','x','p']
print(subsequence(s1,s2,0,0))
#minimum edit distance

def mindist(s1,s2,i,j):
    if i==len(s1) and j==len(s2):
        return 0
    if i==len(s1):
        return len(s2)-j
    if j==len(s2):
        return len(s1)-i
    if s1[i]==s1[j]:
        return mindist(s1,s2,i+1,j+1)
    else:

        x=mindist(s1,s2,i+1,j)+1
        y=mindist(s1,s2,i,j+1)+1
        z=mindist(s1,s2,i+1,j+1)+1
    return min(x,y,z)
s1=['s','a','t','u','r','d','a','y']
s2=['s','u','n','d','a','y']
print(mindist(s1,s2,0,0))
def mindist(s1,s2,i,j):
    if i==len(s1) and j==len(s2):
        return 0
    if i==len(s1):
        return len(s2)-j
    if j==len(s2):
        return len(s1)-i
    if s1[i]==s1[j]:
        return mindist(s1,s2,i+1,j+1)
    else:

        x=mindist(s1,s2,i+1,j)+1
        y=mindist(s1,s2,i,j+1)+1
        z=mindist(s1,s2,i+1,j+1)+1
    return min(x,y,z)+1
s1=['s','a','t','u','r','d','a','y']
s2=['s','u','n','d','a','y']
print(mindist(s1,s2,0,0))



def substring(s1,s2,m,n):
    a = [[0 for k in range(n + 1)] for l in range(m + 1)]
    result=0
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                a[i][j] = 0
            elif (s1[i - 1] == s2[j - 1]):
                a[i][j] = a[i -1][j - 1] + 1
                result = max(result, a[i][j])
            else:
                a[i][j] = 0
    return result

s1=['a','b','a','c','x','g']
s2=['b','a','x','p']
print(substring(s1,s2,len(s1),len(s2)))


# A Top-Down DP implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n, dp):
    if (m == 0 or n == 0):
        return 0

    if (dp[m][n] != -1):
        return dp[m][n]

    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(lcs(X, Y, m, n - 1, dp), lcs(X, Y, m - 1, n, dp))
    return dp[m][n]


# Driver code

X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]

print(f"Length of LCS is {lcs(X, Y, m, n, dp)}")

def subsequence(s1,s2,m,n,dp):
    if (m == 0 or n == 0):
        return 0

    if (dp[m][n] != -1):
        return dp[m][n]

    if s1[m - 1] == s2[n - 1]:
        dp[m][n] = 1 + subsequence(s1, s2, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(subsequence(s1, s2, m, n - 1, dp), subsequence(s1, s2, m - 1, n, dp))
    return dp[m][n]


s1=['a','b','a','c','x','g']
s2=['b','a','x','p']
m=len(s1)
n=len(s2)
dp=[[-1 for _ in range(m+1)]for _ in range(n+1)]
print(subsequence(s1,s2,m,n,dp))


# Dynamic Programming implementation of LCS problem'''

def lcs(X, Y):

    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]


    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))

b=30
def fun(a,b=b):
    return a+b
print(fun(1))