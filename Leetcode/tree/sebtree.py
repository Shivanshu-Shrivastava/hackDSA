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
    
    def isSubtree(self, root, subRoot) -> bool:
        if root:
            if root.value==4:
                print('l',root.value )
                print('l',root.left.value )
                print('l',root.right.value )
                print('s',subRoot.value)
                print('s',subRoot.left.value)
                print('s',subRoot.right.value)
            if root.value==subRoot.value and root.left.value==subRoot.left.value and root.right.value==subRoot.right.value:
                return True
            self.isSubtree(root.left,subRoot)
            self.isSubtree(root.right,subRoot)
        # return False
        



tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(1)
tree.root.left.right = Node(2)

stree = BinaryTree(4)
stree.root.left = Node(1)
stree.root.right = Node(2)

print(tree.isSubtree(tree.root,stree.root))