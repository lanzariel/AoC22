import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

cubes = [tuple([int(i) for i in j.strip().split(',')]) for j in lines]

cubes_set = set(cubes)

ans = 0
deltas = [[0,0,0] for i in range(6)]
for i in range(6):
    if i%2==0:
        deltas[i][i//2] = 1
    else:
        deltas[i][i//2] = -1

for c in cubes:
    ans += 6
    for d in deltas:
        other = tuple([c[i]+d[i] for i in range(3)])
        if other in cubes:
            ans -= 1

print(ans)
