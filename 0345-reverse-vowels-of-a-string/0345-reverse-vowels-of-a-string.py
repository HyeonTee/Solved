class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u', 'A','E','I','O','U'}
        s_list = list(s)
        rev_val = []
        rev_idx = []
        
        for idx, val in enumerate(s_list):
            if val in vowels:
                rev_val.append(val)
                rev_idx.append(idx)
        
        n = len(rev_val)
        for i in range(n):
            s_list[rev_idx[i]] = rev_val[n-1-i]
        
        return ''.join(s_list)
            
                
                