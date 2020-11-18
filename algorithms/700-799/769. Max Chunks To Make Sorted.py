class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr:
            return 0
        res = 0
        currentMax = -float('inf')
        for i, num in enumerate(arr):
            currentMax = max(currentMax, num)
            if currentMax == i:
                res += 1
        return res