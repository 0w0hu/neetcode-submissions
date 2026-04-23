class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
        for n in num:
            if n - 1 not in num:
                curr = 0
                while n+curr in num:
                    curr += 1
                longest = max(curr, longest)
        return longest