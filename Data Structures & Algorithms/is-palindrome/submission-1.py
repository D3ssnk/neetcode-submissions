class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = "".join(letter for letter in s if 
        (letter.isalpha() == True) or (letter.isdigit() == True))
        
        reversed_string = string[::-1]
        if string == reversed_string: return True
        else: return False
    
        