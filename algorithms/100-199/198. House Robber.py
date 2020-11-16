class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr
        return curr
            
            