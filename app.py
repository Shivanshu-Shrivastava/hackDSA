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

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return ""

    # def preorder_search(self, start, find_val):
    #     """Helper method - use this to create a 
    #     recursive search solution."""
    #     return False

    # def preorder_print(self, start, traversal):
    #     """Helper method - use this to create a 
    #     recursive print solution."""
    #     return traversal
    def preorder(self,root):
        
        print(root.value),
        # print (root.data)
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)
    def postorder(self,root):
        print(root.value)
        if root.left == None and root.right == None:
            return print('ye hi hai==',root.value)
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        
        # if root == None:
        #     return True
        # if root.left == None and root.right == None:
        #     return True
        # if root.left == None:
        #     self.preorder(root.right)
               
        # else:
        #     self.preorder(root.left) 
        # print('omggg--',root.value)
        # if root.right == None:
        #     self.preorder(root.left)
        # else:
        #     self.preorder(root.right)
        #     print('khatam')


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.postorder(tree.root))
# Test search
# Should be True
# print (tree.search(tree.root,8))
# Should be False
# print tree.search(6)

# # Test print_tree
# # Should be 1-2-4-5-3
# print tree.print_tree()