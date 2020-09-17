# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.output = 0
        
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.recurse(root, 0, 0, { })
        return self.output
 
    
    def recurse(self, node, pos, depth, d):
        if node == None: return
        
        if depth not in d: d[depth] = pos
        self.output = max(self.output, 1 + pos - d[depth])
        self.recurse(node.left, pos * 2, depth + 1, d)
        self.recurse(node.right, pos * 2 + 1, depth + 1, d)
            