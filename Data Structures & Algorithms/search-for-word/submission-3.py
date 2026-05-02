class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or board[r][c] != word[i]:
                return False

            visit.add((r,c))
            i += 1
            found = (dfs(r+1, c, i) or dfs(r-1, c, i) or dfs(r, c+1, i) or dfs(r, c-1, i))
            visit.remove((r,c))
            return found

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
