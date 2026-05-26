class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = []
        left = 0
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < left:
                heapq.heappop(heap)
            if i+1 >= k:
                output.append(-heap[0][0])
                left += 1
        return output