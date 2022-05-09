def field_farm(n):
    if n==0:
        return 1
    if n==1 :
        return 1
    if n==2:
        return 2
    y=field_farm(n-2)+field_farm(n-1)
    return y

print(field_farm(6))
'''def block_arr(a,m,n):
    if a[m][n]==1:
        return 0
    if m==0 and n==0:
        return 0
    if m==0 :
        return a[m][n-1]
    if n==0 :
        return a[m-1][n]
    x=block_arr(a,m,n-1)
    y=block_arr(a,m-1,n)
    return x+y

a=[[0,0,0,1],
   [0,0,1,0],
   [1,0,0,0],
   [0,0,1,0]]
print(block_arr(a,4,4))'''