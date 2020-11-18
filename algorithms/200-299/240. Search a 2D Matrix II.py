class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        while i <= n - 1 and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                j -= 1
            else:
                i += 1
        return False
        