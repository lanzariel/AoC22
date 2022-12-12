import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


mat = [[int(i) for i in l.strip()] for l in lines]

m = len(mat)
n = len(mat[0])

vis = [[0 for j in range(n)] for i in range(m)]


for i in range(m):
    cur_max = -1
    for j in range(n):
        if mat[i][j] > cur_max:
            cur_max = mat[i][j]
            vis[i][j]=1
    cur_max = -1
    for j in range(n-1, -1, -1):
        if mat[i][j] > cur_max:
            cur_max = mat[i][j]
            vis[i][j]=1

for j in range(n):
    cur_max = -1
    for i in range(m):
        if mat[i][j] > cur_max:
            cur_max = mat[i][j]
            vis[i][j]=1
    cur_max = -1
    for i in range(m-1, -1, -1):
        if mat[i][j] > cur_max:
            cur_max = mat[i][j]
            vis[i][j]=1
print(sum([sum(i) for i in vis]))
