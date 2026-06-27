class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = 0, 0
        res = ""

        while len1 < len(word1) and len2 < len(word2):
            res += word1[len1]
            res += word2[len2]
            len1, len2 = len1+1, len2+1 
        
        if len1 < len(word1):
            res += word1[len1:]

        if len2 < len(word2):
            res += word2[len2:]
        
    

        return res
