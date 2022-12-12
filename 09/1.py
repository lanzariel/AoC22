import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


tail_pos = set()

head = (0,0)
tail = (0,0)

mp = {"R" : (0,1), "L": (0,-1), "U" : (1,0), "D": (-1,0)}

for l in lines:
    drc, it = l.strip().split()
    it = int(it)
    d_mov = mp[drc]
    for i in range(it):
        touching = False

        new_head = (head[0] + d_mov[0], head[1] + d_mov[1])
        if tail in [(head[0]+1, head[1]), (head[0]-1, head[1]), (head[0], head[1]+1), (head[0], head[1]-1)]:
            touching = True
        if touching:
            new_tail = (tail[0] + d_mov[0], tail[1] + d_mov[1])
            if new_tail==head:
                tail = new_tail
        else:
            if max(abs(new_head[0]-tail[0]), abs(new_head[1]- tail[1]))==2:
                tail = head
        tail_pos.add(tail)
        head = new_head
        # print(head, tail)

# print(tail_pos)
print(len(tail_pos))
