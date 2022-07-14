class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self,root):
        if root != None  :
            print(root.value,end=' ')

        if root:
            self.preorder(root.left)
            self.preorder(root.right)
    acc=[]
    def invertTree(self, root) :
        
        if root:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            print(root.value)
        return root
# Set up tree
tree = BinaryTree(4)
tree.root.left = Node(2)
tree.root.right = Node(7)
tree.root.right.left = Node(6)
tree.root.right.right = Node(9)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)

print(tree.invertTree(tree.root))