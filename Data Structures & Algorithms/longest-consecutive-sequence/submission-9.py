class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res = 0

        for n in num:
            i = 0
            while n + i in num:
                i += 1
            res = max(res, i)
        return res
            