class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        s = ''
        stack = []
        for char in chars:
            if not stack or stack[-1] == char:
                stack.append(char)
            else:
                if len(stack) > 1:
                    s += stack[-1] + str(len(stack))
                else:
                    s += stack[-1]
                stack = [char]
        
        if len(stack) > 1:
            s += stack[-1] + str(len(stack))
        else:
            s += stack[-1]
            
        length = len(s)
        
        for i in range(length):
            chars[i] = s[i]
        
        return length