class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        visit = set()
        def dfs(r, c, cur_color):
            
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or image[r][c] != cur_color:
                return
            
            image[r][c] = color
            visit.add((r, c))

            dfs(r+1, c, cur_color)
            dfs(r-1, c, cur_color)
            dfs(r, c+1, cur_color)
            dfs(r, c-1, cur_color)

            visit.remove((r, c))

        dfs(sr, sc, image[sr][sc])
        return image 