# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        q = deque([[root,1]])
        res = []

        while q:
            node, depth = q.popleft()
            if node:
                if len(res) < depth: res.append([])
                res[-1].append(node.val)
                q.append([node.left, depth + 1])
                q.append([node.right, depth + 1])
        
        return res


        