class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) return false;
        int n = matrix.size(), m = matrix[0].size();
        int i = 0, j = m -1;
        while (i <= n-1 && j >= 0){
            int num = matrix[i][j];
            if (num == target){
                return true;
            } else if (num > target){
                j -= 1;
            } else{
                i += 1;
            }
        }
        return false;
    }
};