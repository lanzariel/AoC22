import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

s = lines[0].strip()

fourth = [s[i:i+4] for i in range(len(s)-4)]
# print(len(s), fourth)
blocs = []
for it, el in enumerate(fourth):
    l_string = list(el)
    # print(l_string)
    if len(l_string)==len(set(l_string)):
        blocs.append(it)

print(blocs[0]+4)
