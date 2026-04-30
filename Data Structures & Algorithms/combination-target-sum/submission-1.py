class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        
        def dfs(i, subset, total):
            if total == target:
                output.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return
            subset.append(nums[i])
            dfs(i, subset, total+nums[i])
            subset.pop()
            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return output
            