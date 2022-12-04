import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

def points_old(strat):
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

def points(strat):
    strat = strat.strip()
    other, me = strat.split()
    other = ord(other) - ord("A")
    if me=="X":
        my_strat = (other+2)%3
    elif me=="Y":
        my_strat = other
    else:
        my_strat = (other+1)%3
    return points_old(strat[:2] + chr(ord("X") + my_strat))

#print(list(map(points, lines)))

print(sum(map(points, lines)))
