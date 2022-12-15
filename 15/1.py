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
        delta = distance - abs(s[0]-n)
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
        if cur_val>0
