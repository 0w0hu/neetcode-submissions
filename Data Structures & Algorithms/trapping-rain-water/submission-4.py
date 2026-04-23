class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0
        ml, mr = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                ml = max(height[l], ml)
                water += ml- height[l]
            else:
                r -= 1
                mr = max(height[r], mr)
                water += mr -height[r]
        return water

