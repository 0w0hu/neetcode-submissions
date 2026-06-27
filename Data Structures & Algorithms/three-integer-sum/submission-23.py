class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if n > 0:
                break
            l, r = i+1, len(nums)-1
            while l < r:
                three = nums[l] + nums[r] + n
                if three > 0:
                    r -= 1
                elif three < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res