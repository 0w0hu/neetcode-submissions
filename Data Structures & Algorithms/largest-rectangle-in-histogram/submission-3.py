class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        [7,1,7,2,2,4]
        stack = [] # pair(index, height)
        maxarea = 0

        # pop the previous value when it's smaller
        # calculate the area based on the index and maxheigh

        for i, n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index)) 
                start = index
            stack.append((start, n))

        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea