class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num = set(nums)
        for n in num:
            if n-1 not in num:
                index = 0
                while n+index in num:
                    index += 1
                res = max(res, index)
        return res