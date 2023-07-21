def solution(nums):
    n1 = len(set(nums)) # 포켓몬 종류
    n2 = len(nums)//2 # N/2
    
    return n1 if n2>n1 else n2