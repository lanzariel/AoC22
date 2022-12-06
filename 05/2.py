import sys
import copy

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

for it in range(len(lines)):
    if lines[it].strip()=="":
        split = it

instructions = [i.strip() for i in lines[1+split:]]

# print(instructions)
n_containers = len(lines[split-1].strip().split())

containers = [[] for i in range(n_containers)]

for row in range(split-1):
    cur_col = 1
    for n_cont in range(n_containers):
        if lines[row][cur_col] != " ":
            containers[n_cont].append(lines[row][cur_col])
        cur_col += 4

# print(containers)
for i in range(n_containers):
    containers[i].reverse()

cont_final = copy.deepcopy(containers)

for inst in instructions:
    _, i_n, _, i_from, _, i_to = inst.split()
    i_n = int(i_n)
    i_to=  int(i_to)
    i_from = int(i_from)
    # print(i_n, i_to, i_from)
    moving_stack = cont_final[i_from-1][-i_n:]
    for _ in range(i_n):
        to_move = cont_final[i_from-1].pop()
    cont_final[i_to-1].extend(moving_stack)

print("".join([i[-1] for i in cont_final]))
