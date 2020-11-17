class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        if n <= 2:
            return 0
        dp = [0 for _ in range(n)]
        for i in range(2, n):
            if A[i] + A[i-2] == A[i-1] * 2:
                dp[i] = dp[i-1] + 1
        return sum(dp