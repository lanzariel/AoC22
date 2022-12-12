import sys
from collections import Counter

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


monkeys = [[]]
for l in lines:
    l = l.strip()
    if l == "":
        monkeys.append([])
    else:
        monkeys[-1].append(l)

def clean_m(mkl):
    st_ls = mkl[1].split(": ")[1]
    st_ls = [int(i) for i in st_ls.split(", ")]
    op = mkl[2].split("= old ")[1]
    try:
        n = int(op[1:])
        if op[0]=="+":
            def my_fun(old):
                return old + n
        else:
            def my_fun(old):
                return old * n
    except:
        def my_fun(old):
            return old*old
    dv = int(mkl[3].split("by ")[1])
    m_1 = int(mkl[4].split("monkey ")[1])
    m_2 = int(mkl[5].split("monkey ")[1])
    return [st_ls, my_fun, dv, m_1, m_2]

c_mon = [clean_m(m) for m in monkeys]

activity = [0 for i in c_mon]

BIG_M = 1

for cur_mon in c_mon:
    BIG_M *= cur_mon[2]

for cur_mon in c_mon:
    cur_mon[0] = Counter(cur_mon[0])

for t in range(10000):
    for mon_number, cur_mon in enumerate(c_mon):
        for item, number in cur_mon[0].items():
            item = item % BIG_M
            new_item = cur_mon[1](item)
            m_1 = cur_mon[3]
            m_2 = cur_mon[4]
            if new_item % cur_mon[2]==0:
                other_d = c_mon[m_1][0]
            else:
                other_d = c_mon[m_2][0]
            new_item = new_item % BIG_M
            other_d[new_item] = other_d.get(new_item, 0) + number
            activity[mon_number] += number
        cur_mon[0] = {}
activity.sort()
print(activity[-1]*activity[-2])
