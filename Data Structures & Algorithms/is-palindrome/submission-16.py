class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 
        while l < r:
            while not self.isChar(s[l]) and l < r:
                l += 1
            while not self.isChar(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            
        

    def isChar(self, c) -> bool:
        return (ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z") or 
                ord("0") <= ord(c) <= ord("9"))