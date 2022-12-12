import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


mat = [[int(i) for i in l.strip()] for l in lines]

m = len(mat)
n = len(mat[0])

vis = [[1 for j in range(n)] for i in range(m)]


for i in range(m):
    for j in range(n):
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            cur_i, cur_j = i,j
            cur_i += dx
            cur_j += dy
            cur_dir = 0
            while 0<=cur_i<m and 0<=cur_j<n:
                cur_dir += 1
                # print(cur_i, m, cur_j, n)
                if mat[cur_i][cur_j]>=mat[i][j]:
                    break
                cur_i += dx
                cur_j += dy
            vis[i][j] *= cur_dir
# print(vis)
print(max([max(i) for i in vis]))
