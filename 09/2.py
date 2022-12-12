import sys
import copy

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


tail_pos = set()

head = [(0,0) for i in range(10)]

mp = {"R" : (0,1), "L": (0,-1), "U" : (1,0), "D": (-1,0)}

for l in lines:
    drc, it = l.strip().split()
    it = int(it)
    d_mov = mp[drc]
    for i in range(it):
        new_head = copy.deepcopy(head)
        for cur_pos in range(9):
            if cur_pos==0:
                new_head[cur_pos] = (head[cur_pos][0] + d_mov[0], head[cur_pos][1] + d_mov[1])
            diff = (new_head[cur_pos][0]-head[cur_pos+1][0], new_head[cur_pos][1]- head[cur_pos+1][1])
            # print(diff)
            if max(abs(diff[0]), abs(diff[1]))==2:
                # print('ok')
                if abs(diff[0])==2 and abs(diff[1])==2:
                    new_head[cur_pos+1] = (head[cur_pos+1][0] + diff[0]//2, head[cur_pos+1][1] + diff[1]//2)
                elif abs(diff[0])==2:
                    new_head[cur_pos+1] = (head[cur_pos+1][0] + diff[0]//2, head[cur_pos+1][1] + diff[1])
                else:
                    new_head[cur_pos+1] = (head[cur_pos+1][0] + diff[0], head[cur_pos+1][1]+diff[1]//2)
            if cur_pos == 8:
                head[cur_pos+1] = new_head[cur_pos+1]
                tail_pos.add(new_head[cur_pos+1])
            head[cur_pos] = new_head[cur_pos]
        # print(head)

# print(tail_pos)
print(len(tail_pos))
