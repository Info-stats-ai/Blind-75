class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r == rows or c == cols or 
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # start from pacific (top row + left col) and atlantic (bottom row + right col)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])            # top row → pacific
            dfs(rows-1, c, atl, heights[rows-1][c])  # bottom row → atlantic

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])            # left col → pacific
            dfs(r, cols-1, atl, heights[r][cols-1])  # right col → atlantic

        # cells reachable from BOTH oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res