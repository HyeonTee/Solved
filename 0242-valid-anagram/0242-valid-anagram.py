class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_memo = {}

        for i in s:
            if i not in s_memo:
                s_memo[i] = 1
            else:
                s_memo[i] += 1
        
        t_memo = {}
        for i in t:
            if i not in t_memo:
                t_memo[i] = 1
            else:
                t_memo[i] += 1
        
        for s in s_memo.keys():
            if s not in t_memo or s_memo[s] != t_memo[s]:
                return False
        
        return True