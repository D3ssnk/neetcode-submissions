class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            answer = []

            def backtrack(digit,""):
                if digit > length of digits:
                    append to answer
                    return
                for character in digitToChar[digits[digit]]:
                    backtrack(digit + 1, string + charater)
        """
        

        if digits == "": return []
        digitToChar = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "qprs",
                    "8": "tuv",
                    "9": "wxyz",
                }
        answer = []
        def backtrack(digit, string):
            if digit == len(digits):
                answer.append(string)
                return
            for c in digitToChar[digits[digit]]:
                backtrack(digit + 1, string + c)
        
        backtrack(0, "")
        return answer         

        