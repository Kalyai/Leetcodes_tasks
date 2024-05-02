import collections


class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        def dfs(r, c):
            def valid_coords(r, c):
                return 0 <= r < len(grid) and 0 <= c < len(grid[0])

            area = 1
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                row, col = q.popleft()
                for nx, ny in neighbors:
                    r = row + nx
                    c = col + ny
                    if valid_coords(r, c) \
                            and (r, c) not in visited \
                            and grid[r][c] == 1:
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
            return area

        max_area = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(dfs(r, c), max_area)
        return max_area
