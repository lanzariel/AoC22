import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

elves = [[]]

for line in lines:
    if line.strip()=="":
        elves.append([])
    else:
        elves[-1].append(int(line.strip()))

sums = map(sum, elves)

print(max(sums))
