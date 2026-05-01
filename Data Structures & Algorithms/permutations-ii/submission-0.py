class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i):
            if i >= len(nums):
                return [[]]
            
            perm = helper(i+1)
            newperm = []
            for p in perm:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    newperm.append(pcopy)

                    if j < len(p) and p[j] == nums[i]:
                        break
            return newperm
        return helper(0)
        
