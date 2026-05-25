class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        output = 0
        for i in range(len(height)):
            left = right = height[i]

            for j in range(i):
                left = max(left, height[j])
            for j in range(i+1, len(height)):
                right = max(right, height[j])
            
            output += min(left, right) - height[i]
        return output