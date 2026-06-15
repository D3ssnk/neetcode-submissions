# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        def dfs(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False
        
        stack = [root]
        node = None
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    ans = dfs(node,subRoot)
                    if ans: break 
                stack.append(node.left)
                stack.append(node.right)
    
       
        return ans

        