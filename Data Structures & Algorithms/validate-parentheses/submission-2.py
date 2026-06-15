class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")" : "(", "]":"[", "}":"{"}
        for c in s:
            if c in brackets and stack != []:
                if stack[-1] == brackets[c]:
                    stack.pop()
                else: return False
            else: stack.append(c)

        return True if not stack else False 
        