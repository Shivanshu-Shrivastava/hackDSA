from collections import defaultdict
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


def topView(root):
    # Write your code here
    if root is None:
        return None
    queue = [(root, 0)]
    hashtable = defaultdict(list)
    for node, level in queue:
        if node is not None:
            hashtable[level].append(node.value)
        if node.left is not None:
            queue.extend([(node.left, level - 1)])
        if node.right is not None:
            queue.extend([(node.right, level + 1)])
    if hashtable:
        print('hash',hashtable)
        for level in range(min(hashtable.keys()),
                           max(hashtable.keys()) + 1):
            print(hashtable[level][0], end=' ')
    else:
        return None
       
       



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(6)
tree.root.right.right.right.right = Node(8)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(topView(tree.root))