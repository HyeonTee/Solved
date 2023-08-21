class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] == 0:
                del nums[idx]
                cnt += 1
                idx -= 1
            idx += 1
            
        nums += [0] * cnt