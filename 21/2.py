import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

d = {}
for line in lines:
    key, expr = line.strip().split(': ')
    d[key] = expr
symbols = [' + ', ' - ', ' * ', ' / ', ' == ']
for s in symbols:
    if s in d['root']:
        l, r = d['root'].split(s)
        d['root'] = l + ' == ' + r
        break


def get_number(monkey, real_d):
    monkey_expr = real_d[monkey]
    for s in symbols:
        if s in monkey_expr:
            l_m, r_m = monkey_expr.split(s)
            l_val = get_number(l_m, real_d)
            r_val = get_number(r_m, real_d)
            real_d[monkey] = str(eval(l_val + s + r_val))
            break
    return real_d[monkey]

def guess(i):
    my_d = {key : el for key, el in d.items()}
    my_d['humn'] = str(i)
    return float(get_number('pgtp', my_d)) - float(get_number('vrvh', my_d))

def secant(initial_guess, max_attempts = 100, thresh = 100):
    prev_x = initial_guess
    prev_y = guess(prev_x)
    cur_x = initial_guess+1000
    for it in range(max_attempts):
        cur_y = guess(cur_x)
        if abs(cur_y)<thresh:
            return int(cur_x)
        prev_x, prev_y, cur_x = cur_x, cur_y, prev_x - prev_y/((prev_y-cur_y)/(prev_x-cur_x))
    return int(prev_x)

ans = secant(1000)
print('ans = ', ans, guess(ans))
