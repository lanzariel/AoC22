import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

groups = []
for it, el in enumerate(lines):
    if it%3==0:
        groups.append([])
    groups[-1].append(el.strip())

def processer(bag):
    bset = [set(list(b)) for b in bag]
    both = bset[1].intersection(bset[2])
    tri = bset[0].intersection(both)
    el = tri.pop()
    #print(list(bag[:n//2]), list(bag[n//n:]))
    #print(b1, b2)
    # print(both, el)
    if el==el.lower():
        return 1 + ord(el) - ord('a')
    else:
        return ord(el) -ord('A') + 27

print(sum(map(processer, groups)))
