class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        while 0 in nums:
            nums.remove(0)
            cnt += 1
            
        nums += [0] * cnt