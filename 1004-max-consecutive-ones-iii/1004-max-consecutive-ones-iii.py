class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lt = 0
        max_len = 0
        
        for rt in range(n):
            if nums[rt] == 0:
                k -= 1
            
            if k < 0:
                if nums[lt] == 0:
                    k += 1
                lt += 1

            
        return rt - lt + 1