import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

def unitize(d):
    ans = []
    for el in d:
        if el==0:
            ans.append(0)
        else:
            ans.append(int(el/abs(el)))
    return tuple(ans)

max_y = 0
for l in lines:
    l = l.strip()
    pair_list = [tuple([int(i) for i in j.split(",")]) for j in l.split(" -> ")]
    for x,y in pair_list:
        max_y = max(max_y, y)
max_y += 3
grid = [["." for i in range(max_y)] for j in range(1000)]


for l in lines:
    l = l.strip()
    pair_list = [tuple([int(i) for i in j.split(",")]) for j in l.split(" -> ")]
    current_p = pair_list[0]
    grid[current_p[0]][current_p[1]] = "#"
    for other_p in pair_list[1:]:
        # print(" HEYYY", current_p, other_p)
        delta = unitize((other_p[0]-current_p[0], other_p[1]-current_p[1]))
        if delta ==(0,0):
            pass 
            # print(current_p, other_p)
        else:
            while current_p!=other_p:
                current_p = (current_p[0] + delta[0], current_p[1]+delta[1])
                # print(current_p)
                grid[current_p[0]][current_p[1]] = "#"


for row in grid:
    row[-1]="#"

top_touched = False
fallen_units = 0
while not top_touched:
    cur_pos = (500, 0)
    movable = True
    while movable:
        if grid[cur_pos[0]][cur_pos[1]+1]==".":
            cur_pos = (cur_pos[0], cur_pos[1]+1)
        elif grid[cur_pos[0]-1][cur_pos[1]+1]==".":
            cur_pos = (cur_pos[0]-1, cur_pos[1]+1)
        elif grid[cur_pos[0]+1][cur_pos[1]+1]==".":
            cur_pos = (cur_pos[0]+1, cur_pos[1]+1)
        else:
            movable = False
            if cur_pos[1]==0:
                top_touched = True
    grid[cur_pos[0]][cur_pos[1]] = "o"
    fallen_units += 1

# for i in range(480,520):
#    print("".join(grid[i]))


print(fallen_units)
