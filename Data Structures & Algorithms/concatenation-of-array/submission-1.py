class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = 2 * size * [0]

        for i, n in enumerate(nums):
            ans[i] = ans[i+size] = n
                
            
        return ans