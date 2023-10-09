class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                
                stack.pop()
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                
                stack.append(num * substr)
                
        return ''.join(stack)