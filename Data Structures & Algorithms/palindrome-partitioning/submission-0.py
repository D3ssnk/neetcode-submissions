class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        def backtrack(index, array):
            string = ""
            if index == len(s):
                answer.append(array.copy())
                return
            for i in range(index, len(s), 1):
                string += s[i]
                if string == string[::-1]:
                    array.append(string)
                    backtrack(i + 1, array)
                    array.pop()
        
        backtrack(0,[])
        print(answer)
        return answer
        