class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        for num, count in counts.items():
            freq[count].append(num)

        output = []
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output