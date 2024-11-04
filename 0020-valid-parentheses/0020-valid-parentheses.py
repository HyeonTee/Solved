class Solution:
    def isValid(self, s: str) -> bool:        
        def isMatched(c):
            if not stack: return False
            if c == ')' and stack.pop() != '(': return False
            if c == ']' and stack.pop() != '[': return False
            if c == '}' and stack.pop() != '{': return False
            return True
        
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not isMatched(c):
                    return False
        return not stack