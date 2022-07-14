class Node(object):
    def __init__(self, value):
        self.val = value
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
    
    def rangeSumBST(self, root, low, high):
        # 1st method
        # q=[root]
        # sum=low+high
        # while q:
        #     temp = q.pop(0)
        #     if temp.val>low and temp.val<high:
        #         sum+=temp.val
        #     if temp.left:
        #         q.append(temp.left)
        #     if temp.right:
        #         q.append(temp.right)
        # return sum
#         2nd method

        
        if root is None:
            return
        if root:
            if root.val>=low and root.val<=high:
                res = root.val
            else:
                res= 0
        if root:
            # print(root.left.val)
            # # print(root.left.val)
            # print(res,'res')
            # print(res+self.rangeSumBST(root.left,low,high),'rrrr')
        # if root.right != None:
            self.rangeSumBST(root.right,low,high)+res+self.rangeSumBST(root.left,low,high)


tree = BinaryTree(10)
tree.root.left = Node(5)
tree.root.right = Node(15)
tree.root.right.right = Node(18)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)



print(tree.rangeSumBST(tree.root,7,15))