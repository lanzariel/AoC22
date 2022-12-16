import sys
import heapq

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

sb = []


# BIGN = 4000000
BIGN = 20
for l in lines:
    l = l.strip()[12:]
    raw_split = l.split(": closest beacon is at x=")
    real_split = [[max(0,min(int(i),BIGN)) for i in j.split(', y=')] for j in raw_split]
    sb.append(real_split)

def get_occupied(n):
    limits = []
    for s, b in sb:
        distance = abs(s[0]-b[0]) + abs(s[1]-b[1])
        delta = distance - abs(s[1]-n)
        if delta>=0:
            cur_left = s[0] - delta
            cur_right = s[0] + delta
            heapq.heappush(limits, (cur_left, -1))
            heapq.heappush(limits, (cur_right, 1))

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

ans = 0
for i in range(BIGN+1):
    if get_occupied(i)!=BIGN+1:
        ans += i
print(ans)


            
