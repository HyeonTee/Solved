from itertools import combinations

def is_prime(num):
    ok = True
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            ok = False
    return ok

def solution(nums):
    answer = 0
    sum_list = []
    for comb in combinations(nums, 3):
        sum_list.append(sum(comb))
    
    for n in sum_list:
        if is_prime(n):
            answer += 1
            
    return answer