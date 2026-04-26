class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for n in nums:
            cursum = max(0, cursum)
            cursum += n
            maxsum = max(maxsum, cursum)
        return maxsum