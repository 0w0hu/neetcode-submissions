class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] *2 * size
        for i, n in enumerate(nums):
            ans[i] = ans[i+size] = n
        return ans