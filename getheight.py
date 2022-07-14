class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self,root, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        print(root.value)
        if root.value == find_val:
            return True
        if root == None or root.left == None or root.right == None:
            print('yaha se ret')
            
            return False
        if self.search(root.left,find_val) == True:

            print('left---',root.left.value)
            return True
        elif self.search(root.right,find_val) == True:
            print('right---',root.right.value)

            return True
        return False
    
    def getHeight(self,root):
        #Write your code here
        leftHeight = 0
        rightHeight = 0
        if( root.left):            
            leftHeight = self.getHeight(root.left) + 1
            print('letfvaluee',root.left.value)

            print('letf',leftHeight)
            
        if( root.right):
            rightHeight = self.getHeight(root.right) + 1
            print('rightvaluee',root.right.value)

            print('right',rightHeight)

       
        if( leftHeight > rightHeight ):
            return leftHeight
        else:
            return rightHeight
        



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.getHeight(tree.root))