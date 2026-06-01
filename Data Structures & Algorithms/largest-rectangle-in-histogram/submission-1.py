class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i,val in enumerate(heights):
            start = i
            while stack and stack[-1][1] > val:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, val))
        
        for i,height in stack:
            maxArea = max(maxArea, height * (len(heights)-i))
        return maxArea