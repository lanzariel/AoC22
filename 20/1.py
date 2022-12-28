import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


original = [int(i.strip()) for i in lines]

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


    def swap(self, n1, n2):
        if n1.prev:
            n1.prev.post = n2
        else:
            self.root = n2
        if n1.post:
            n1.post.prev = n2
        else:
            self.last = n2
        if n2.prev:
            n2.prev.post = n1
        else:
            self.root = n1
        if n2.post:
            n2.post.prev = n1
        else:
            self.last = n1
        n1.prev, n1.post, n2.pre, n2.post = n2.prev, n2.post, n1.prev, n2.post

    def insert_post(self, n1, n2):
        if n1==n2:
            pass
        else:
            if n1.prev:
                n1.prev.post = n1.post
            else:
                self.root= n1.post
            if n1.post:
                n1.post.prev = n1.prev
            else:
                self.last = n1.prev
            if n2.post:
                n2.post.prev = n1
            else:
                self.last = n1

        n2.post, n1.prev, n1.post = n1, n2, n2.post

    def find(self, val):
        pos = 0
        cur_node = self.root
        # print(cur_node.val, val)
        while cur_node.val!=val:
            # print(cur_node, val)
            cur_node = cur_node.post
        return  cur_node

    def move_right_old(self, node, steps):
        cur_node = node
        while steps>0:
            if cur_node==self.last:
                cur_node=self.root
            else:
                cur_node = cur_node.post
            steps-=1
        return cur_node

    def move_right(self, node, steps):
        if steps<0:
            return self.move_left(node, -steps+1)
        elif steps==0:
            return node
        cur_node = node
        if cur_node==self.last:
            cur_node=self.root
        else:
            cur_node = cur_node.post
        while steps>1:
            if cur_node==node:
                steps+=1
            if cur_node==self.last:
                cur_node=self.root
            else:
                cur_node = cur_node.post
            steps-=1
        return cur_node
    
    def move_left(self, node, steps):
        cur_node = node
        if cur_node==self.root:
            cur_node = self.last
        else:
            cur_node = cur_node.prev

        while steps>1:
            if cur_node==node:
                steps+=1
            if cur_node==self.root:
                cur_node = self.last
            else:
                cur_node = cur_node.prev
            steps-=1
        return cur_node

    def perform_step(self, val):
        to_move = self.find(val)
        destination = self.move_right(to_move, val[1])
        self.insert_post(to_move, destination)

    def solve(self, lst):
        self.print()
        for it, el in enumerate(lst):
            self.perform_step((it,el))
            print("===") 
            self.print()
            if el==0:
                self.zero_val = (it,el)

    def print(self):
        cur_node = self.root
        while cur_node!=self.last:
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
s.solve(original)
print(s.produce_ans_1())
