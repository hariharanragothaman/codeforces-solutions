# Understood the question

from collections import defaultdict
from collections import deque
# We have figured out the data structure to represent

class NTree:
    def __init__(self):
        self.hmap = defaultdict(list)

    def add_node(self, parent, node):
        if parent == -1:
            self.hmap[0].append(node)
        else:
            self.hmap[parent].append(node)

if __name__ == '__main__':
    n = int(input())
    t = NTree()
    i = 1
    while i <= n:
        t.add_node(int(input()), i)
        i += 1

    #print("The map is:", t.hmap)
    levels = 0
    node = t.hmap[0]
    q = deque([node])
    #print(q)

    level_children = []
    while q:
        #print("The queue is:", q)
        np = q.popleft()
        #print("The node is:", np)
        level_children = []
        for node in np:
            if node in t.hmap:
                for child in t.hmap[node]:
                    level_children.append(child)
        #print("The level children are:", level_children)
        if level_children:
            q.append(level_children)
        levels += 1

    print(levels)