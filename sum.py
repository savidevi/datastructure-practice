'''class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        flag=False
        for i in range(n-1):
            for j in range(n-1):
                if i<n-1:
                    t = nums[i] + nums[j + 1]
                    if t == target and i!=j+1:
                        output=[i, j + 1]
                        print(output)
                        flag=True

            if flag:
                break

num = [2,5,5,11]
s1 = Solution()
s1.twoSum(num, 10)
b=121
a=str(b)
#print(len(a))
i=1
while i<=len(a):
    st=a[-i]
    i+=1
    print(int(st),end="")
if a==st:
    print("yes")
else:
    print("no")

class Solution(object):
    def isPalindrome(self, x):
        st=str(x)
        n=len(st)
        i=1
        while i<=n:
            b=st[-i]
            i+=1
            t=print(str(b),end="")
        h=int(t)
        if x==h:
            print("yes")
        else:
            print("no")
s1=Solution()
s1.isPalindrome(121)'''
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")