class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
                
        return max(memo, key=memo.get)