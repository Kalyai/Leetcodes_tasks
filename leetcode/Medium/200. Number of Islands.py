import collections

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(r, c):
            def valid_coord(r, c):
                return 0 <= r < len(grid) and 0 <= c < len(grid[0])

            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for nx, ny in neighbors:
                    r = row + nx
                    c = col + ny
                    if valid_coord(r, c) \
                    and (r, c) not in visited \
                    and grid[r][c] == '1':
                        visited.add((r, c))
                        q.append((r, c))
                        dfs(r, c)

        visited = set()
        islands = 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands