class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            val = 1
            for k in new_nums:
                val *= k
            output.append(val)
        return output