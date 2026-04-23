class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        ans = nums[r]
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            m = (l+r)//2
            ans = min(nums[m], ans)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ans