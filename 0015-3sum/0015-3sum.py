class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        memo = {}
        for num in nums:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
        
        if 0 in memo and memo[0] >= 3:
            ans.add((0,0,0))
        
        nums = list(set(nums))
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if -(nums[i]+nums[j]) in memo:
                    if -(nums[i]+nums[j]) != nums[i] and -(nums[i]+nums[j]) != nums[j]:
                        ans.add(tuple(sorted([-(nums[i]+nums[j]), nums[i], nums[j]])))
                    
                    if -(nums[i]+nums[j]) == nums[i] or -(nums[i]+nums[j]) == nums[j]:
                        if memo[-(nums[i]+nums[j])] > 1:
                            ans.add(tuple(sorted([-(nums[i]+nums[j]), nums[i], nums[j]])))
        
        
        return ans