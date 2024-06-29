def solution(participant, completion):
    answer = ''
    memo = {}
    for p in participant:
        if p in memo:
            memo[p] += 1
        else:
            memo[p] = 1
            
    for c in completion:
        memo[c] -= 1
        
    for key, value in memo.items():
        if value == 1:
            answer = key
    return answer