def solution(nums):
    n = len(nums)
    k = len(set(nums))
    
    if n/2 <= k:
        return n/2
    
    return k