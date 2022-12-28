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
        # t_sum = lambda x, y : ((rows + x[0]+y[0])%rows, (cols+x[1]+y[1])%cols)
        # I guess I'll do it by hand?
        # I'm sorry, incentives are towards using my specific input here
        def t_sum(x,y):
            n_pos = (x[0]+y[0] , x[1]+y[1])
            if n_pos[0] == -1:
                if n_pos[1]<50: # A
                    n_pos = (50+n_pos[1],0)
                    y = (0,1)
                elif n_pos[1]<100: # B
                    n_pos = (150 + n_pos[1]-50, 0)
                    y = (0, 1)
                else: # C
                    n_pos = (rows-1, n_pos[1]-100)
                    y = (-1, 0)
            elif n_pos[0] == rows:
                if n_pos[1]<50: # C
                    n_pos = (0, n_pos[1]+100)
                    y = (1, 0)
                elif n_pos[1]<100: #D
                    n_pos = (150+n_pos[1]-50, cols-1)
                    y = (0, -1)
                else: # E
                    n_pos = (50 + n_pos[1]-100, cols-1)
                    y = (0, -1)

            if n_pos[1] == -1:
                if n_pos[0]<50: # F
                    n_pos = (150 - 1 - n_pos[0], 0)
                    y = (0, 1)
                elif n_pos[0]<100: # A
                    n_pos = (0, n_pos[0]-50)
                    y = (1,0)
                elif n_pos[0]<150: # F
                    n_pos = (150-1-n_pos[0], 0)
                    y = (0,1)
                else: # B
                    n_pos = (0, 50+n_pos[0]-150)
                    y = (1,0)
            elif n_pos[1] == cols:
                if n_pos[0]<50: # G
                    # print("HEY", n_pos, cols-1, 150-1-n_pos[0])
                    n_pos = (150 -1 -n_pos[0], cols-1)
                    y = (0, -1)
                elif n_pos[0]<100: # E
                    n_pos = (rows-1, 100+n_pos[0]-50)
                    y = (-1, 0)
                elif n_pos[0]<150: # G
                    n_pos = (150-1 - n_pos[0], cols-1)
                    y = (0, -1)
                else: # D
                    n_pos = (rows-1, 50+ n_pos[0]-150)
                    y = (-1, 0)
            return n_pos, y
        next_pos, next_direction = t_sum(self.pos, self.direction)
        while m_map[next_pos[0]][next_pos[1]]==' ':
            next_pos, next_direction = t_sum(next_pos, next_direction)
        return next_pos, next_direction

    def move(self, n):
        for it in range(n):
            succ, new_direction = self.next_square()
            if m_map[succ[0]][succ[1]]=='.':
                self.pos = succ
                self.direction = new_direction
            else:
                break

    

w = Walker()
cur_n = 0
# print(w.pos)
# print(rows, cols)
for el in inst_line:
    if el in "1234567890":
        cur_n = 10*cur_n + int(el)
    else:
        if cur_n>0:
            w.move(cur_n)
            # print(cur_n, (w.pos[1], w.pos[0]), (w.direction[1], w.direction[0]))
            cur_n = 0
        if el=="R":
            # print('R')
            w.turn_right()
        elif el=="L":
            # print('L')
            w.turn_left()

dir_converter = {(0,1) : 0, (1,0) : 1, (0,-1) : 2, (-1,0) : 3}

# for i in m_map:
#     print(i)

print(1000*(w.pos[0]+1)+4*(w.pos[1]+1)+dir_converter[w.direction])
