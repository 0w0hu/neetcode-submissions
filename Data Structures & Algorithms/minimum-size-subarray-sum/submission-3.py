class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        output = float("inf")
        l = 0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum >= target:
                output = min(output, r-l+1)
                cursum -= nums[l]
                l += 1
                
            
        return output if output != float("inf") else 0