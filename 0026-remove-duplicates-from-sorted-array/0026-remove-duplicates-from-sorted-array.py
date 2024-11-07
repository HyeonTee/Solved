class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        temp = -101
        for i in range(len(nums)):
            if temp != nums[i]:
                nums[k] = nums[i]
                temp = nums[i]
                k += 1
        
        return k