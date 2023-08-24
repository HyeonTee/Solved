class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        memo = {}
        cnt = 0
        for num in nums:
            target = k - num
            if target in memo and memo[target] > 0:
                memo[k-num] -= 1
                cnt += 1
                
            else:
                memo[num] = memo.get(num, 0) + 1
        return cnt