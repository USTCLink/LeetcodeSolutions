class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        prev, curr = 1, 1
        for _ in range(n-1):
            prev, curr = curr, prev + curr
        return curr