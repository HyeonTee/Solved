class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        if n == 1:
            if s in t:
                return True
            else:
                return False
        
        i = 0
        for target in t:
            if target == s[i]:
                i += 1
                if i == n:
                    return True
        
        return False