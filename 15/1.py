import sys
import heapq

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

sb = []

for l in lines:
    l = l.strip()[12:]
    raw_split = l.split(": closest beacon is at x=")
    real_split = [[int(i) for i in j.split(', y=')] for j in raw_split]
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
        if b[1]==n:
            heapq.heappush(limits, (b[0], 0))

    ans = 0
    cur_pos = -float('inf')
    cur_val = 0
    seen_b = set()
    while len(limits)>0:
        next_pos, pos_type = heapq.heappop(limits)
        # print(next_pos, pos_type, cur_val, cur_pos,ans)
        if cur_val>0 and pos_type==-1:
            cur_val += 1
        elif cur_val>0 and pos_type==1:
            cur_val -= 1
            if cur_val==0:
                ans += next_pos - cur_pos
        elif cur_val>0 and pos_type==0:
            if not next_pos in seen_b:
                ans -=1 # all different I hope
                seen_b.add(next_pos)
        elif cur_val==0 and pos_type==-1:
            ans += 1
            cur_pos = next_pos
            cur_val = 1
    return ans
print(get_occupied(2000000))


            
