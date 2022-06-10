'''def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
data = [1,2,3]
for p in permutation(data):
    print(p)
from itertools import permutations
t=list(permutations([1,2,3]))
print(t)
'''

def perm(str,j):
    if j>=len(str):
        print(str)
        return
    for i in range(j,len(str)):
        str[j],str[i]=str[i],str[j]
        perm(str,j+1)
        str[j], str[i] = str[i], str[j]

str=[1,2,3]
perm(str,0)