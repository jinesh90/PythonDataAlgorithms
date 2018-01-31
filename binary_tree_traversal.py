"""
Example of various tree traversal
Original Tree is

         A
    B          C
D      E    F     G

"""
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


inorder_traversal_list = []
preorder_traversal_list = []
postorder_traversal_list = []


def inorder_traversal(tree):
    if tree is not None:
        inorder_traversal(tree.left)
        inorder_traversal_list.append(tree.data)
        inorder_traversal(tree.right)


def preorder_traversal(tree):
    if tree is not None:
        preorder_traversal_list.append(tree.data)
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)


def postorder_traversal(tree):
    if tree is not None:
        postorder_traversal(tree.left)
        postorder_traversal(tree.right)
        postorder_traversal_list.append(tree.data)


inorder_traversal(tree)
preorder_traversal(tree)
postorder_traversal(tree)


print("INORDER TRAVERSAL: {}".format(inorder_traversal_list))
print("PREORDER TRAVERSAL: {}".format(preorder_traversal_list))
print("POSTORDER TRAVERSAL: {}".format(postorder_traversal_list))

