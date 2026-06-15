# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root
        pv = p.val
        qv = q.val

        while curr:
            if pv < curr.val and qv < curr.val: curr = curr.left
            elif pv > curr.val and qv > curr.val: curr = curr.right
            else: return curr