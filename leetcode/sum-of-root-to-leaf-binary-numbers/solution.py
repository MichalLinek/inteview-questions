# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.recurse(root, str(root.val))
    
    def recurse(self, node, numString):
        if not node.left and not node.right:
            return int(numString, 2)
        
        sum1 = 0
        sum2 = 0
        
        if node.left:
            sum1 = self.recurse(node.left, numString + str(node.left.val))
        if node.right:
            sum2 = self.recurse(node.right, numString + str(node.right.val))
        return sum1 + sum2