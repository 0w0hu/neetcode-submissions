class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i, cur):
            if cur == word:
                print("Found")
                return True
            
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or board[r][c] != word[i]:
                return False
            
            cur += board[r][c]
            visit.add((r,c))
            found = (dfs(r+1, c, i+1, cur) or dfs(r-1, c, i+1, cur) or dfs(r, c+1, i+1, cur) or dfs(r, c-1, i+1, cur))
            visit.remove((r,c))
            return found

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, ""):
                    return True
        return False
