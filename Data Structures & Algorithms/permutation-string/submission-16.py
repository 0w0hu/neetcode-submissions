class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, window = {}, {}
        
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i], 0)
        
        if count1 == window:
            return True
        
        l = 0 
        for r in range(len(s1), len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            if window == count1:
                return True
        return False