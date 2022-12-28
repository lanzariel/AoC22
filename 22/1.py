import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

m_map = []
inst_line = -1
for it, l in enumerate(lines):
    if l=='\n':
        inst_line = lines[it+1] + "."
        break
    m_map.append(l[:-1])



rows = len(m_map)
cols = max([len(i) for i in m_map])
m_map = [i.ljust(cols, ' ') for i in m_map]

t_sum = lambda x, y : ((rows + x[0]+y[0])%rows, (cols+x[1]+y[1])%cols)

class Walker:
    def __init__(self):
        for it, el in enumerate(m_map[0]):
            if el=='.':
                self.pos = (0,it)
                break
        self.direction = (0,1)

    def turn_right(self):
        self.direction = (self.direction[1], -self.direction[0])

    def turn_left(self):
        self.direction = (-self.direction[1], self.direction[0])

    def next_square(self):
        next_pos = t_sum(self.pos, self.direction)
        while m_map[next_pos[0]][next_pos[1]]==' ':
            next_pos = t_sum(next_pos, self.direction)
        return next_pos

    def move(self, n):
        for it in range(n):
            succ = self.next_square()
            if m_map[succ[0]][succ[1]]=='.':
                self.pos = succ
            else:
                break

    

w = Walker()
cur_n = 0
for el in inst_line:
    if el in "1234567890":
        cur_n = 10*cur_n + int(el)
    else:
        if cur_n>0:
            w.move(cur_n)
            cur_n = 0
            # print(w.pos)
        if el=="R":
            w.turn_right()
        elif el=="L":
            w.turn_left()

dir_converter = {(0,1) : 0, (1,0) : 1, (0,-1) : 2, (-1,0) : 3}

# for i in m_map:
#     print(i)

print(1000*(w.pos[0]+1)+4*(w.pos[1]+1)+dir_converter[w.direction])
