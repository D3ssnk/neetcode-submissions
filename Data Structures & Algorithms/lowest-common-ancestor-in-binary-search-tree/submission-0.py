# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        stack = [[root,[]]]
        paths = []
        hashm = {}

        while stack:
            node, path = stack.pop()
            if node:
                hashm[node.val] = node
                if node.val == p.val or node.val == q.val:
                    paths.append(path + [node.val])
            
                stack.append((node.left, path + [node.val]))
                stack.append((node.right,path + [node.val]))
        
        seen = set(paths[1])
        rev = paths[0][::-1]
        for value in rev:
            if value in seen:
                target = value
                break
        
        
        return hashm[target]