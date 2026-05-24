class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for k in range(i+1, len(numbers)):
                if numbers[i] + numbers[k] == target:
                    return [i+1, k+1]
        return []