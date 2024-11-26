class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n = 200
        for s in strs:
            n = min(n, len(s))
            
        for i in range(n):
            fix = strs[0][i]
            flag = True
            for s in strs:
                if fix != s[i]:
                    flag = False
                    break
            if flag:
                prefix += fix
            else:
                break
                
        return prefix