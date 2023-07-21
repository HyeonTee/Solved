def solution(participant, completion):
    participant.sort()  # 참가자 목록 정렬
    completion.sort()  # 완주자 목록 정렬
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 완주자 목록을 모두 비교한 후에도 반복이 종료되지 않았다면
    # 마지막 참가자가 완주하지 못한 선수임
    return participant[-1]