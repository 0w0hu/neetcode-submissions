class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def helper(i):
            if i >= len(nums):
                return [[]] 

            perm = helper(i+1)
            nextperm = []
            for p in perm:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    nextperm.append(pcopy)
            return nextperm

        res = helper(0)
        return res            