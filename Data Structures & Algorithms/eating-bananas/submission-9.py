class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l+r) // 2
            
            # condition m can eat all banana in the given hours:
            hour = 0
            for p in piles:
                hour += math.ceil(p/m)
            if hour <= h:
                res = m
                r = m - 1
            # in other case, hour > h
            else:
                l = m + 1
            
        return res
