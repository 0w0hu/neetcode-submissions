class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()

        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            if r-l+1 > k:
                seen.remove(nums[l])
                l += 1
        return False

            
            