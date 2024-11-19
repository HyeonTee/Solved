class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        lt = 0
        rt = len(s) - 1
        while lt <= rt:
            while lt < rt and not s[lt].isalnum():
                lt += 1
            while lt < rt and not s[rt].isalnum():
                rt -= 1

            if s[lt].lower() != s[rt].lower():
                return False
            lt += 1
            rt -= 1
        
        return True