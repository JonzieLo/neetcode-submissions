class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] or nums == None:
            return 0
        count = 1
        chain = 1
        nums_sorted = sorted(list(set(nums)))
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i-1] + 1:
                chain += 1
                if chain > count:
                    count = chain
            else:
                chain = 1
        return count
            