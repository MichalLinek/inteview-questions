# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.w = 0
        self.recurse(root, distance)
        return self.w
        
    def recurse(self, root, distance):
        if not root: return []
        if root.left == None and root.right == None: return [0]
        
        left = self.recurse(root.left, distance)
        right = self.recurse(root.right, distance)
        
        left = [i + 1 for i in left if i + 1 <= distance]
        right = [i + 1 for i in right if i + 1 <= distance]
        
        for i in left:
            for j in right:
                if i + j <= distance:
                    self.w += 1
        
        return left + right