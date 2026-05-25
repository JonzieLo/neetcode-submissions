class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                area = min(heights[left], heights[right]) * (right - left)
                if area > output:
                    output = area

        return output
