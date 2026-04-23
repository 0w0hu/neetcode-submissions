class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        water = 0

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                water += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                water += maxr - height[r]
        return water