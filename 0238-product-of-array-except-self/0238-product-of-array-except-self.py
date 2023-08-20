class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pro_all = 1
        zero_idx = []
        for i in range(n):
            if nums[i] == 0:
                zero_idx.append(i)
                continue
            pro_all *= nums[i]
        
        ans = [0] * n
        
        if len(zero_idx) > 1:
            return ans
        elif len(zero_idx) == 1:
            ans[zero_idx[0]] = pro_all
            return ans
        else:
            for i in range(n):
                ans[i] = pro_all // nums[i]
            return ans