import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

KEY = 811589153
original = [KEY*int(i.strip()) for i in lines]

class Node:
    def __init__(self, val=0, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class SlowSolver:
    def __init__(self, lst):
        self.root = Node((0, lst[0]))
        self.last = self.root
        self.n = len(lst)
        for it, el in enumerate(lst[1:]):
            new_node = Node((it+1, el), prev=self.last)
            self.last.post = new_node
            self.last = new_node
        self.last.post = self.root
        self.root.prev= self.last



    def extract(self, n1):
        n1.prev.post = n1.post
        n1.post.prev = n1.prev
        if self.root==n1:
            self.root=n1.post

    def insert_post(self, n1, n2):
        if n1==n2:
            pass
        else:
            n2.post.prev = n1
            n2.post, n1.prev, n1.post = n1, n2, n2.post

    def find(self, val):
        pos = 0
        cur_node = self.root
        while cur_node.val!=val:
            cur_node = cur_node.post
        return  cur_node

    def move_right_old(self, node, steps):
        cur_node = node
        while steps>0:
            cur_node = cur_node.post
            steps-=1
        return cur_node

    def move_right(self, node, steps):
        if steps<0:
            return self.move_left(node, -steps)
        cur_node = node
        steps = steps%(self.n-1)
        while steps>0:
            cur_node = cur_node.post
            steps-=1
        return cur_node
    
    def move_left(self, node, steps):
        cur_node = node.prev
        steps = steps%(self.n-1)
        while steps>0:
            cur_node = cur_node.prev
            steps-=1
        return cur_node

    def perform_step(self, val):
        if val[1]!=0:
            to_move = self.find(val)
            self.extract(to_move)
            destination = self.move_right(to_move, val[1])
            self.insert_post(to_move, destination)

    def solve(self, lst):
        for it, el in enumerate(lst):
            self.perform_step((it,el))
            if el==0:
                self.zero_val = (it,el)

    def print(self):
        cur_node = self.root
        while cur_node!=self.root.prev:
            print(cur_node)
            cur_node = cur_node.post
        print(cur_node)

    def produce_ans_1(self):
        ans = 0
        cur_pos = self.find(self.zero_val)
        for i in range(3):
            cur_pos = self.move_right_old(cur_pos,1000)
            ans += cur_pos.val[1]
        return ans
s = SlowSolver(original)
for i in range(10):
    s.solve(original)
print(s.produce_ans_1())
