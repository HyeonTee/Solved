class Solution:
    def twoSum(self, nums, target) -> List[int]:
        memo = {}
        
        for i, num in enumerate(nums):
            if target - num in memo:
                return [memo[target-num], i]
            else:
                memo[num] = i