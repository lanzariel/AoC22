import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

def prio(bag):
    bag = bag.strip()
    n = len(bag)
    b1 = set(list(bag[:n//2]))
    b2 = set(list(bag[n//2:]))
    both = b1.intersection(b2)
    el = both.pop()
    #print(list(bag[:n//2]), list(bag[n//n:]))
    #print(b1, b2)
    # print(both, el)
    if el==el.lower():
        return 1 + ord(el) - ord('a')
    else:
        return ord(el) -ord('A') + 27

print(sum(map(prio, lines)))
