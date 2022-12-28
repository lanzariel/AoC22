import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

d = {}
for line in lines:
    key, expr = line.strip().split(': ')
    d[key] = expr
symbols = [' + ', ' - ', ' * ', ' / ']

def get_number(monkey):
    monkey_expr = d[monkey]
    for s in symbols:
        if s in monkey_expr:
            l_m, r_m = monkey_expr.split(s)
            l_val = get_number(l_m)
            r_val = get_number(r_m)
            d[monkey] = str(int(eval(l_val + s + r_val)))
            break
    return d[monkey]

print(get_number('root'))
