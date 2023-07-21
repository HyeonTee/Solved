def find_max(counts):
    result = []
    count_max = max(counts)
    
    for i, count in enumerate(counts):
        if count_max == count:
            result.append(i+1)
    return result

def solution(answers):
    ans_count = [0, 0, 0]
    st1 = [1, 2, 3, 4, 5] * 2000
    st2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i in range(len(answers)):
        if answers[i] == st1[i]:
            ans_count[0] += 1
        if answers[i] == st2[i]:
            ans_count[1] += 1
        if answers[i] == st3[i]:
            ans_count[2] += 1
    
    return find_max(ans_count)