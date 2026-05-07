class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1

        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            
            old_curmax = curmax
            curmax = max(n, curmax * n, curmin * n)
            curmin = min(n, old_curmax * n, curmin * n)
            res = max(res, curmax, curmin)
        
        return res