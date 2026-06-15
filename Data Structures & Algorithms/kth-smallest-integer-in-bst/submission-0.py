# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        stack2 = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                stack2.append(curr.val)
                curr = curr.left
            print(stack2)
            curr = stack.pop()
            stack.append(curr.right)
            k -= 1
            if k == 0: return curr.val
            else: curr = stack.pop()
            
        
        

        