class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = {}
        for a in arr:
            if a not in memo:
                memo[a] = 0
            else:
                memo[a] += 1
                
        occur = list(memo.values())
        if len(occur) == len(set(occur)):
            return True
        else:
            return False