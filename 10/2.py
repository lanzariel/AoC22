import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

reg = 1
ans = ["." for i in range(240)]
cycle = 0
for it, l in enumerate(lines):
    l = l.strip()
    if abs(reg-(cycle%40))<=1:
        ans[cycle] = "#"
    cycle += 1
    if l[0]=="a":
        if abs(reg-(cycle%40))<=1:
            ans[cycle] = "#"
        cycle+=1
        inst, val = l.split()
        val = int(val)
        reg += val

real_ans = []
for it, el in enumerate(ans):
    if it%40==0:
        real_ans.append([el])
    else:
        real_ans[-1].append(el)
print("\n".join(["".join(i) for i in real_ans]))
