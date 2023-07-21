permutations = []

def permutation(curr, remains):
    if not remains:
        permutations.append(curr)
        return
    for i in range(len(remains)):
        new_curr = curr + [remains[i]]
        new_remains = remains[:i] + remains[i+1:]
        permutation(new_curr, new_remains)

def solution(k, dungeons):
    answer = 0
    
    permutation([], dungeons)
    
    for p in permutations:
        cnt = 0
        fatigue = k
        for dungeon in p:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                cnt += 1
        answer = max(answer, cnt)
    
    return answer