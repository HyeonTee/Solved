def longest_chain(start, end):
    longest = []
    current = []
    
    def is_valid(curr, next):
        return (curr % next == 0) or (next % curr == 0)
    
    def explore(curr):
        nonlocal longest, current
        current.append(curr)
        
        for next in range(start, end + 1):
            if next not in current and is_valid(curr, next):
                explore(next)
        
        if len(longest) < len(current):
            longest = current.copy()
        
        current.pop()
        
    for init in range(start, end+1):
        explore(init)
    
    return longest

start = 1
end = 10

longest = longest_chain(start, end)
print(longest)