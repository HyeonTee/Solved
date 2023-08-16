def solution(targets):
    answer = 1
    targets.sort(key = lambda x: x[1])
    
    missile = targets[0][1] - 0.5
    for target in targets:
        if missile <= target[0]:
            answer += 1
            missile = target[1] - 0.5
    
    return answer