class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])

        left = 0
        right = r*c - 1
        while left <= right:
            mid = left + (right-left) // 2
            row = mid // c
            col = mid % c
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
        return False