class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        output = nums[0]
        while left <= right:
            if nums[left]< nums[right]:
                return min(output, nums[left])
                break
            mid = (left + right)//2
            output = min(output, nums[mid])
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        return output

