import numpy as np
def blocked_mat(m,n):
    if a[m][n]==0:
        return 0
    if m==0 and n==0:
        return 0
    if m==0:
        return a[m][n-1]
    if n==0:
        return a[m-1][n]
    x= blocked_mat(m-1,n)
    y=blocked_mat(m,n-1)
    return x+y

a=np.array([[1,1,0,1],[1,1,1,1],[0,1,0,1],[1,1,1,1]])
print(blocked_mat(3,3))
#memorization
def blocked_mat(m,n):
    if a[m][n]==0:
        return 0
    if m==0 and n==0:
        return 0
    if m==0 :
        return a[m][n-1]
    if n==0:
        return a[m-1][n]
    a[m][n]=blocked_mat(m-1,n)+blocked_mat(m,n-1)
    return a[m][n]
a=np.array([[1,1,0,1],[1,1,1,1],[0,1,0,1],[1,1,1,1]])
print(blocked_mat(3,3))
#dp
def blocked_mat(a,m,n):

    for i in range(m):
        if a[i][0]==0:
            a[i][0]=1
        else:
            break
    for j in range(n):
        if a[0][j]==0:
            a[0][j] =1
        else:
            break
    for i in range(1,m):
        for j in range(1,n):
            if a[i][j]==0:
                continue
            if a[i-1][j]>0:
                a[i][j]=(a[i-1][j]+a[i][j])
            else:
                a[i][j] = a[i][j-1] + a[i][j]

    return a[m-1][n-1],a
a=[[1,1,0,1],[1,1,1,1],[0,1,0,1],[1,1,1,1]]
print(blocked_mat(a,4,4))


'''R = 4
C = 4

def countPaths(maze):

    if (maze[0][0] == -1):
        return 0

    for i in range(R):
        if (maze[i][0] == 0):
            maze[i][0] = 1

        else:
            break

    for i in range(1, C, 1):
        if (maze[0][i] == 0):
            maze[0][i] = 1

        else:
            break

    for i in range(1, R, 1):
        for j in range(1, C, 1):

            if (maze[i][j] == -1):
                continue

            if (maze[i - 1][j] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i - 1][j])

            if (maze[i][j - 1] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i][j - 1])

    if (maze[R - 1][C - 1] > 0):
        return maze[R - 1][C - 1],maze
    else:
        return 0
if __name__ == '__main__':
    maze = [[0, 0, -1, 0],
            [0, 0, 0, 0],
            [-1, 0, -1, 0],
            [0, 0, 0, 0]]
    print(countPaths(maze))'''