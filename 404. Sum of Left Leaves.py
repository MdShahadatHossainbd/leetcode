# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0

        def sumOfLeftLeaves(root, isLeft):
            if isLeft and root.left == None and root.right == None:
                self.sum += root.val
                return
            if root.left != None: sumOfLeftLeaves(root.left, True)
            if root.right != None: sumOfLeftLeaves(root.right, False)

        if root == None: return 0
        sumOfLeftLeaves(root, False)
        return self.sum