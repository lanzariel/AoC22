with open("input.txt", "r") as f:
    lines = f.readlines()

maze = [list(i.strip()) for i in lines]

m = len(maze)
n = len(maze[0])

for row in range(m):
    for col in range(n):
        if maze[row][col]=="S":
            maze[row][col]="a"
            start = (row,col)
        if maze[row][col]=="E":
            maze[row][col]="z"
            end = (row,col)

visited = set([start])
cur_places = [start]

steps = 0
done = False
while len(cur_places)>0:
    next_places = []
    for row,col in cur_places:
        for delta in [(0,1), (0,-1), (1,0), (-1,0)]:
            row_new = row + delta[0]
            col_new = col + delta[1]
            pos_new = (row_new, col_new)
            if not (0<=row_new<m and 0<=col_new<n ):
                continue
            if not pos_new in visited:
                if ord(maze[row_new][col_new]) - ord(maze[row][col])<=1:
                    next_places.append(pos_new)
                    visited.add(pos_new)
                    if pos_new == end:
                        done = True
        if done:
            break
    steps += 1
    if done:
        break
    else:
        cur_places = next_places
print(steps)
