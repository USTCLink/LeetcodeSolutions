class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {}; 
        int n = matrix.size(), m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m, INT_MAX - 1));
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (matrix[i][j] == 0){
                    dp[i][j] = 0;
                } else {
                    if (i > 0){
                        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j]);
                    }
                    if (j > 0){
                        dp[i][j] = min(dp[i][j-1] + 1, dp[i][j]);
                    }
                }
            }
        }
        for (int i = n-1; i >= 0; --i){
            for (int j = m-1; j >= 0; --j){
                if (matrix[i][j] != 0){
                    if (i < n-1){
                        dp[i][j] = min(dp[i+1][j] + 1, dp[i][j]);
                    }
                    if (j < m-1){
                        dp[i][j] = min(dp[i][j+1] + 1, dp[i][j]);
                    }
                }
            }
        }
        return dp;
    }
};