import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

reg = 1
ans = 0
cycle = 1
for it, l in enumerate(lines):
    l = l.strip()
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(cycle*reg)
        ans += cycle*reg
    if l[0]=="a":
        cycle+=1
        inst, val = l.split()
        val = int(val)
        reg += val
        if cycle in [20, 60, 100, 140, 180, 220]:
            # print(cycle*reg)
            ans += cycle*reg
print(ans)
