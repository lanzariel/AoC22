import sys
import re
import itertools
import tqdm
import math

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

nbs = {}

valves = {}

for l in lines:
    my_re = re.search(r'Valve (.*?) has flow rate=(.*?); tunnel(s)? lead(s)? to valve(s)? (.*)', l.strip())
    nbs[my_re.group(1)] = my_re.group(6).split(', ')
    valves[my_re.group(1)] = int(my_re.group(2))


n = len(nbs)
converter = {lett : num for num, lett in enumerate(nbs.keys())}
nbs_nums = {converter[key] : [converter[i] for i in el] for key, el in nbs.items()}
valves_nums = {converter[key] : val for key, val in valves.items()}

fw = [[float('inf') for j in range(n)] for i in range(n)]

for v, friends in nbs_nums.items():
    fw[v][v] = 0
    for el in friends:
        fw[v][el] = 1

for z in range(n):
    for x in range(n):
        for y in range(n):
            other = fw[x][z] + fw[z][y]
            new_val = min(fw[x][y], other, fw[y][x])
            fw[x][y] = new_val
            # fw[y][x] = new_val

nz_valves = [k for k, val in valves_nums.items() if val>0]

def total_val(lst):
    minute = 0
    ans = 0
    cur_pos = converter['AA']
    for new_pos in lst:
        minute += fw[cur_pos][new_pos] + 1 
        # print("move", fw[cur_pos][new_pos])
        if minute >30:
            break
        ans += (30 - minute ) * valves_nums[new_pos]
        # print("Valve value", valves_nums[new_pos], "cur min", minute)
        cur_pos = new_pos
    return ans


class FullSolver:
    cur_ans = 0
    cur_sol = [converter['AA']]
    def __init__(self):
        self.cur_ans = 0
        self.cur_sol = [converter['AA']]
    def rec_solver(self, pre, cur_total, cur_minute, remainings, upper_hand):
        if upper_hand < self.cur_ans:
            return cur_total # Or upper_hand
        if len(remainings)==0 or cur_minute >= 30:
            return cur_total
        best_ans = 0
        for next_valve in remainings:
            next_minute = cur_minute + fw[pre[-1]][next_valve] + 1
            next_rems = [i for i in remainings if i!=next_valve]
            next_pre = pre.copy()
            next_pre.append(next_valve)
            if next_minute <= 30:
                next_total = cur_total + (30-next_minute)*valves_nums[next_valve]
                # print(30-next_minute,  valves_nums[next_valve], next_total)
                next_rems_copy = next_rems.copy()
                next_upper = next_total + self.upper_calculator(next_minute, next_rems_copy)
                next_ans = self.rec_solver(next_pre, next_total, next_minute, next_rems, next_upper)
                # print(next_pre, next_rems, next_total, "t= ", next_minute, next_upper)
                if next_total>self.cur_ans:
                    self.cur_ans = next_total
                    self.cur_sol = next_pre
                best_ans = max(best_ans, next_ans)
        return best_ans
    def upper_calculator(self, pos, lst):
        remaining_values = [valves_nums[i] for i in lst]
        ans = 0
        while pos<=30 and len(remaining_values)>0:
            pos += 1
            ans += remaining_values.pop() * (30-pos)
        return ans

    def solve(self):
        upper_estimate = self.upper_calculator(0, nz_valves)
        return self.rec_solver([converter['AA']], 0, 0, nz_valves, upper_estimate)

s = FullSolver()
s.solve()
print(s.cur_ans)
print(s.cur_sol)

# perms = itertools.permutations(nz_valves)
# ans = -float('inf')
# winning_one = None
# print("Total elements to permute: ", len(nz_valves))
# for p in tqdm.tqdm(perms, total = math.factorial(len(nz_valves))):
#     cur_tot = total_val(p)
#     if cur_tot>ans:
#         ans = cur_tot
#         winning_one = p
# print(ans)
