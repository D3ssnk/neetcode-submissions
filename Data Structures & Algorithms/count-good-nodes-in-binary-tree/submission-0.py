# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root, []]]
        res = 0


        while stack:
            node, path = stack.pop()
            if node:
                path = path + [node.val]
                stack.append([node.left, path])
                stack.append([node.right, path])
                if max(path) == node.val: res += 1
        return res

        