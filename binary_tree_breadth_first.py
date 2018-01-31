"""
Example of breadth first tree traversal
Original Tree is:

         A
    B          C
D      E    F     G

"""
from collections import deque

# Single Node define

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

# Tree define

tree = Node('A')
tree.left = Node('B')
tree.right = Node('C')
tree.left.left = Node('D')
tree.left.right = Node('E')
tree.right.left = Node('F')
tree.right.right = Node('G')



def breadth_first_traversal(tree):
    q = deque()
    q.append(tree)

    while len(q) != 0:
        node = q.popleft()
        print(node.data)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


breadth_first_traversal(tree)
