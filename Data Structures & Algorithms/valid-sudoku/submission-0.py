class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen: return False
                    seen.add(val)

        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen: return False
                    seen.add(val)
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[row+i][col+j]
                        if val != '.':
                            if val in seen: return False
                            seen.add(val)
        return True