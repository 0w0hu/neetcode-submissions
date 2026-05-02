class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set() # r+c
        negdiag = set() # r-c

        res = []
        board = [["."]*n for i in range(n)]

        def helper(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r+c in posdiag or r-c in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"
                
                helper(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        helper(0)
        return res