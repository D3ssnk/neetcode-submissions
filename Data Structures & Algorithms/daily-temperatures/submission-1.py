class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            if stack == []: stack.append((temp,i))
            elif stack[-1][0] >= temp: stack.append((temp,i)) 
            elif stack[-1][0] < temp:
                while stack[-1][0] < temp:
                    answer[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                    if stack == []: break
                stack.append((temp,i))

        return answer 