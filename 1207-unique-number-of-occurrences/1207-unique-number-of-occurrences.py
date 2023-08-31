class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = {}
        for a in arr:
            if a not in memo:
                memo[a] = 1
            else:
                memo[a] += 1
        
        occurs = list(memo.values())
        
        return len(occurs) == len(set(occurs))