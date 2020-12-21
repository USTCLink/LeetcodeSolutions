class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        d = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while queue:
            r, c, d = queue.popleft()
            for _ in range(4):
                i = r + dx[_]
                j = c + dy[_]
                if 0 <= i < n and 0 <= j < m:
                    if grid[i][j] == 1 and (i,j) not in visited:
                        queue.append((i, j, d + 1))
                        visited.add((i, j))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        return d
        
        
        