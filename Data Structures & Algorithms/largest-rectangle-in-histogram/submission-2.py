class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] # (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, hei = stack.pop()
                maxarea = max(maxarea, hei * (i - ind))
                start = ind
            stack.append((start, h))

        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea
