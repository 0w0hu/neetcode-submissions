class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        largest = 0
        
        for n in num:
            if n-1 not in num:
                i = 0
                while n + i in num:
                    i += 1
                largest = max(largest, i)
        return largest
                