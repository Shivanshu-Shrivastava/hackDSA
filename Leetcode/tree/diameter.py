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
    def preorder(self,root):
        if root != None  :
            print(root.value,end=' ')

            # print('root==',root.value)
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
       
        # if root != None  :
        
        #     print('run--',root.value)
        # print(root.value,end = ' ')
        # if root.left == None and root.right == None :
        #     return
        # if root.left is not None:
        #     self.preorder(root.left)
        # if root.right is not None:
        #     self.preorder(root.right)
    def diameter(self,root):
        dia=0
        def dfs(root):
            if not root:
                return 0
            left_height=dfs(root.left)
            print('left',left_height)
            right_height=dfs(root.right)
            print('right',right_height)
            nonlocal dia
            dia=max(dia,right_height+left_height)
            print(dia,'dia')
            return 1+max(right_height,left_height)
    
        dfs(root)
        return dia



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.diameter(tree.root))