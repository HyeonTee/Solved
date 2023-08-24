class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        memo = {}
        cnt = 0
        for num in nums:
            if ((k-num) in memo) and memo[k-num] > 0:
                memo[k-num] -= 1
                cnt += 1
                
            else:
                memo[num] = memo.get(num, 0) + 1
        return cnt