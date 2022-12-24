import sys
import math


path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

shapes = [
        ['####'],
        ['.#.', '###', '.#.'],
        ['..#', '..#', '###'],
        ['#', '#', '#', '#'],
        ['##', '##']
        ]

moves= lines[0].strip()

class Game:
    def __init__(self):
        self.game = ['#######']
        for i in range(3):
            self.game.append('.......')
        self.top_row = -1

    def clear(self):
        while self.game and not '#'in self.game[-1]:
            self.game.pop()
        self.top_row = len(self.game)-1
        for i in range(3):
            self.game.append('.......')

    def throw(self, obj):
        self.clear()
        self.cur_obj = obj
        for i in range(len(self.cur_obj)):
            self.game.append('.......')
        self.cur_pos = (len(self.game),2)

    def move(self, delta):
        self.cur_pos = (self.cur_pos[0] + delta[0], self.cur_pos[1] + delta[1])

    def can_move(self, delta):
        new_pos = (self.cur_pos[0] + delta[0], self.cur_pos[1] + delta[1])
        for dx in range(len(self.cur_obj)):
            cur_x = new_pos[0] - dx
            for dy in range(len(self.cur_obj[0])):
                cur_y = new_pos[1] + dy
                # print(new_pos, (dx, dy), (cur_x, cur_y), len(self.game))
                if cur_y <0 or cur_y>=7:
                    return False
                elif self.cur_obj[dx][dy]=='#' and self.game[cur_x][cur_y]=='#':
                    return False
        return True

    def fix(self):
        for dx in range(len(self.cur_obj)):
            cur_x = self.cur_pos[0] - dx
            self.game[cur_x] = list(self.game[cur_x])
            for dy in range(len(self.cur_obj[0])):
                cur_y = self.cur_pos[1] + dy
                if self.cur_obj[dx][dy]=='#':
                    self.game[cur_x][cur_y]= '#'
            self.game[cur_x] = "".join(self.game[cur_x])

    def print(self):
        for el in self.game[::-1]:
            print(el)
        print("============")
g = Game()
move_n = 0
obj_n = 0
n = 0

# 
excel_like = []

while n < 100000:
    g.throw(shapes[obj_n])
    while g.can_move((-1,0)):
        g.move((-1,0))
        if moves[move_n] == "<":
            if g.can_move((0,-1)):
                g.move((0,-1))
        else:
            if g.can_move((0,1)):
                g.move((0,1))
        move_n += 1
        move_n = move_n % len(moves)
    g.fix()
    n += 1
    obj_n += 1
    obj_n = obj_n % len(shapes)
    excel_like.append([n, obj_n, move_n, g.top_row])

small_excel = [el[1:3] for el in excel_like]


for p in range(1,10000):
    if small_excel[-100:]==small_excel[-100-p:-p]:
        period = p
        break
# print(period)

delta = excel_like[-1][-1] - excel_like[-1-period][-1]
BIGN = 1000000000000
rep = math.ceil((BIGN-50000)/period)
row = BIGN - period*rep
print(excel_like[row][-1] + delta*rep)
