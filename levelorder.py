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
            if root.value not in acc:
                acc.append(root.value)
            if root.left:
                acc.append(root.left.value)
            if root.right:
                acc.append(root.right.value)
            
            self._preOrder(root.left, acc)
            self._preOrder(root.right, acc)
            # acc.append(root.value)
            print(acc)

    def levelOrder(self,root):
        acc = []
        
        self._preOrder(root,acc)
        # print(acc)
        print(" ".join(map(str, acc)))#for changing list to digit [1,2]=>1 2
        #Write your code here
        
def levelOrder(root):
    myQ = [root]
    print(myQ[0].value,'myq')
    li=[]
    while(len(myQ) > 0):
        iter = myQ.pop(0)
        # print(iter.value)
        print(iter.value,'iterval',end = " ")
        if (iter.left != None):
            # print('left',myQ)

            myQ.append(iter.left)
            li.append(iter.left.value)
        if (iter.right != None):
            # print('right',myQ)

            myQ.append(iter.right)
            li.append(iter.right.value)
        print(li,'li')



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(levelOrder(tree.root))