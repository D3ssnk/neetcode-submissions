# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        pq = deque([p])
        qq = deque([q])
        pval, qval = [],[]
        while pq:
            node = pq.popleft()
            if node:
                pval.append(node.val)
                pq.append(node.left)
                pq.append(node.right)
            else:
                pval.append(-101)
        
        while qq:
            node = qq.popleft()
            if node:
                qval.append(node.val)
                qq.append(node.left)
                qq.append(node.right)
            else:
                qval.append(-101)
        


        return pval == qval