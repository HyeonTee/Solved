class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        n = len(x_str)
        for i in range(n // 2 + 1):
            if x_str[i] != x_str[n-i-1]:
                return False
        return True