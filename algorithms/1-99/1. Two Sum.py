class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target-num]]
            if num not in dic:
                dic[num] = i
        