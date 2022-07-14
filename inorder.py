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
    
    def _preOrder(self,root, acc):
        if root:
            self._preOrder(root.left, acc)
            self._preOrder(root.right, acc)
            acc.append(root.value)
            print(acc)
        

    def inOrder(self,root):
        # acc=[]
        # if root :
        #     self.inOrder(root.left)
        #     self.inOrder(root.right)
        #     acc.append(root.value)
        # acc = sorted(acc)
        # print(acc)
        acc = []
        self._preOrder(root, acc)
        a=sorted(acc)
        print(" ".join(map(str, a)))#for changing list to digit [1,2]=>1 2
        #Write your code here
        



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.inOrder(tree.root))