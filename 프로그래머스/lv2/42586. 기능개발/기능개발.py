from collections import deque

def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
    
    curr = progresses[0]
    cnt = 1
    for i in range(1, len(progresses)):
        if curr >= progresses[i]:
            cnt += 1
        else:
            curr = progresses[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    print(progresses)
    return answer