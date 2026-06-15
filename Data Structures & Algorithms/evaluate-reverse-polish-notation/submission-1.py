class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pop_values = {"+", "-", "*", "/"}
        stack = []
        placeholder = 0
        for item in tokens:
            if item in pop_values:
                if item == "+": placeholder = int(stack[-2]) + int(stack[-1])
                if item == "-": placeholder = int(stack[-2]) - int(stack[-1])
                if item == "*": placeholder = int(stack[-2]) * int(stack[-1])
                if item == "/": placeholder = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(placeholder)
            else:
                stack.append(item)
            
        return int(stack[-1])


                

        