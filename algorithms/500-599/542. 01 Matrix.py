class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1) 
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1) 
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][j] != 0:
                    if j < m-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1) 
                    if i < n-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1) 
                    
        return dp