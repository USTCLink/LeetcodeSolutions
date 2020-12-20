class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res
                