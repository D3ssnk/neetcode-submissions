class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        answer = []

        def parenth(openN, closedN):
            if openN == closedN == n:
                answer.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                parenth(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                parenth(openN, closedN + 1)
                stack.pop()
        parenth(0,0)
        return answer
        