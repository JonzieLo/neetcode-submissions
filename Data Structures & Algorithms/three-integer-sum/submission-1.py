class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            start = i+1
            end = len(nums) - 1
            while start < end:
                sums = num + nums[start] + nums[end]
                if sums < 0:
                    start += 1
                elif sums > 0:
                    end -= 1
                else:
                    output.append([num, nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
        return output