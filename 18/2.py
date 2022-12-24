import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

cubes = [tuple([int(i) for i in j.strip().split(',')]) for j in lines]

cubes_set = set(cubes)

deltas = [[0,0,0] for i in range(6)]
for i in range(6):
    if i%2==0:
        deltas[i][i//2] = 1
    else:
        deltas[i][i//2] = -1

def count_faces(c_s):
    ans = 0
    for c in c_s:
        ans += 6
        for d in deltas:
            other = tuple([c[i]+d[i] for i in range(3)])
            if other in c_s:
                ans -= 1
    return ans

limits = [[] for i in range(3)]
for i in range(3):
    col = [el[i] for el in cubes]
    limits[i] = [min(col)-1, max(col)+1]

all_cubes = set()

for x in range(limits[0][0], limits[0][1]+1):
    for y in range(limits[1][0], limits[1][1]+1):
        for z in range(limits[2][0], limits[2][1]+1):
            all_cubes.add((x,y,z))

external = set([(limits[0][0], limits[1][0], limits[2][0])])
processing = list(external)
while len(processing)>0:
    cur_el = processing.pop()
    for d in deltas:
        other = tuple([cur_el[i] + d[i] for i in range(3)])
        if other in all_cubes and not other in external and not other in cubes_set:
            external.add(other)
            processing.append(other)

print(count_faces(external) - count_faces(all_cubes))

