class Solution:
    def twoSum(self, nums, target) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            rest = target - n
            if rest in dict:
                return [dict[rest], i]
            else:
                dict[n] = i