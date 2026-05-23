class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()

                key = (r // 3, c // 3)
                if key not in squares:
                    squares[key] = set()
                
                if val in rows[r] or val in cols[c] or val in squares[key]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[key].add(val)
        return True
