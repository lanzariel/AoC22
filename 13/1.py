import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


pairs = [[]]

for line in lines:
    line = line.strip()
    if line=="":
        pairs.append([])
    else:
        pairs[-1].append(eval(line))

def order(l1, l2):
    # print(l1, l2)
    l1_int = isinstance(l1, int)
    l2_int = isinstance(l2, int)
    if l1_int and l2_int:
        if l1<l2:
            return 0
        elif l1==l2:
            return 1
        else:
            return 2
    elif l1_int:
        return order([l1], l2)
    elif l2_int:
        return order(l1, [l2])
    else:
        if len(l1)==0 and len(l2)==0:
            return 1
        elif len(l1)==0:
            return 0
        elif len(l2)==0:
            return 2
        else:
            fo = order(l1[0], l2[0])
            if fo!=1:
                return fo
            else:
                return order(l1[1:], l2[1:])

is_sorted = [order(el[0], el[1]) for el in pairs]
# print(is_sorted)

print(sum([it+1 for it,el in enumerate(is_sorted) if el==0]))
