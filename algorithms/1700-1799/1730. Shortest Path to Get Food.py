class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    x, y = i, j
        queue = collections.deque()
        queue.append((x, y, 0))
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        dis = -1
        while queue:
            dis += 1
            for k in range(len(queue)):
                i, j, distance = queue.popleft()
                if grid[i][j] == '#':
                    return dis
                grid[i][j] = 'X'
                for _ in range(4):
                    x = i + dx[_]
                    y = j + dy[_]
                    if x >= 0 and x < n and y >= 0 and y < m:
                        if grid[x][y] != 'X':
                            queue.append((x, y, distance + 1))
        return -1