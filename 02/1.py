import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

def points(strat):
    strat = strat.strip()
    other, me = strat.split()
    other = ord(other) - ord("A")
    me = ord(me) - ord("X")
    ans = me + 1
    # print(other, me)
    if other == ((me+1)%3):
        return ans 
    if other == me:
        return ans +3
    if ((other +1)%3)==me:
        return ans + 6

#print(list(map(points, lines)))

print(sum(map(points, lines)))
