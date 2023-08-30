class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        lt = 0
        
        for rt in range(n):
            if nums[rt] == 0:
                k -= 1
            
            if k < 0:
                if nums[lt] == 0:
                    k += 1
                lt += 1

        return rt - lt