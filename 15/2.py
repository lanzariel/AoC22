import sys
import heapq
import tqdm

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

sb = []


BIGN = 4000000
# BIGN = 20
for l in lines:
    l = l.strip()[12:]
    raw_split = l.split(": closest beacon is at x=")
    real_split = [[int(i) for i in j.split(', y=')] for j in raw_split]
    sb.append(real_split)
# print(sb)
def get_occupied(n, my_sb):
    limits = []
    for s, b in my_sb:
        distance = abs(s[0]-b[0]) + abs(s[1]-b[1])
        delta = distance - abs(s[1]-n)
        if delta>=0:
            cur_left = s[0] - delta
            cur_right = s[0] + delta
            heapq.heappush(limits, (max(0,min(cur_left, BIGN)), -1))
            heapq.heappush(limits, (max(0,min(cur_right, BIGN)), 1))

    ans = 0
    cur_pos = -float('inf')
    cur_val = 0
    while len(limits)>0:
        next_pos, pos_type = heapq.heappop(limits)
        # print(next_pos, pos_type, cur_val, cur_pos,ans)
        if cur_val>0 and pos_type==-1:
            cur_val += 1
        elif cur_val>0 and pos_type==1:
            cur_val -= 1
            if cur_val==0:
                ans += next_pos - cur_pos
        elif cur_val==0 and pos_type==-1:
            ans += 1
            cur_pos = next_pos
            cur_val = 1
    return ans

ans_y = 0
for i in tqdm.tqdm(range(BIGN+1)):
    if get_occupied(i, sb)!=BIGN+1:
        print(i, get_occupied(i, sb))
        ans_y += i



print(ans_y)


sb_trans = []
for a,b in sb:
    new_a = (a[1], a[0])
    new_b = (b[1], b[0])
    sb_trans.append([new_a, new_b])


ans_x = 0
for i in tqdm.tqdm(range(BIGN+1)):
    if get_occupied(i, sb_trans)!=BIGN+1:
        print(i, get_occupied(i, sb_trans))
        ans_x += i


print(4000000*ans_x + ans_y)
