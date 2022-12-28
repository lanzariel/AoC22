import sys
import tqdm 

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

grid_raw = []
for l in lines[1:-1]:
    l = l[1:-2]
    grid_raw.append(l)
rows = len(grid_raw)
cols = len(grid_raw[0])

converter = {'>' : (0, 1), '<' : (0, -1), '^' : (-1, 0), 'v' : (1, 0)}

class Hurricane:
    def __init__(self, kind, x, y, rows, cols):
        self.pos = (x,y)
        self.dir = converter[kind]
        self.rows = rows
        self.cols = cols

    def move(self):
        self.pos = ((rows + self.pos[0]+self.dir[0])%rows, (cols+self.pos[1]+self.dir[1])%cols)

class Grid:
    def __init__(self, g_raw):
        self.rows = len(g_raw)
        self.cols = len(g_raw[0])
        self.hurricanes = []
        for r_num, row_raw in enumerate(g_raw):
            for c_num, el in enumerate(row_raw):
                if el in '<>^v':
                    self.hurricanes.append(Hurricane(el, r_num, c_num, self.rows, self.cols))
        self.get_free()

    def move(self):
        for h in self.hurricanes:
            h.move()
        self.get_free()

    def get_free(self):
        occupied = set()
        for h in self.hurricanes:
            occupied.add(h.pos)
        self.free = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if not (r,c) in occupied:
                    self.free.add((r,c))

    def get_nbs(self, row, col):
        nbs = []
        # if row<1 and col ==0:
        #     nbs.append((-1,0))
        for dr in (-1, 0 ,1):
            for dc in (-1, 0, 1):
                candidate = (row+dr, col+dc) 
                if 0<=candidate[0]<self.rows and 0<=candidate[1]<self.cols and candidate in self.free:
                    if dr*dc==0:
                        nbs.append(candidate)
        return nbs

def get_least_d(real_raw_g, starting, ending):
    g = Grid(real_raw_g)
    processing = [starting]
    it = 0
    for it in range(1000000):
        g.move()
        next_processing = set()
        for cur_pos in processing:
            nb_list = g.get_nbs(cur_pos[0], cur_pos[1])
            for cur_nb in nb_list:
                if cur_nb==ending:
                    return it
                elif cur_nb in g.free:
                    next_processing.add(cur_nb)
        processing = next_processing
        processing.add(starting)


print(get_least_d(grid_raw, (-1,0), (rows-1,cols-1)) + 2)


