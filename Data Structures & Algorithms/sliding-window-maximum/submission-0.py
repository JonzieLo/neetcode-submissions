class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums)-k+1):
            window = max(nums[i:k+i])
            output.append(window)

        return output