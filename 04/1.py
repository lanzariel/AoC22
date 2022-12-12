import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

def a_contains_b(a,b):
    return a[0]<=b[0] and a[1]>=b[1]

def consider(ass):
    ass = ass.strip()
    e1, e2 = ass.split(',')
    to_tup = lambda x : tuple(map(int, x.split('-')))
    e1 = to_tup(e1)
    e2 = to_tup(e2)
    if a_contains_b(e1, e2) or a_contains_b(e2, e1):
        return 1
    else:
        return 0

print(sum(map(consider, lines)))

