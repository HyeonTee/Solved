class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        lt = 1
        for i in range(n):
            ans[i] *= lt
            lt *= nums[i]
        
        rt = 1
        for i in range(n-1,-1,-1):
            ans[i] *= rt
            rt *= nums[i]
        
        return ans