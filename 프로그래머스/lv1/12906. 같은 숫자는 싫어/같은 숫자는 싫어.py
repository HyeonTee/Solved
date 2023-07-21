def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    curr = arr[0]
    answer.append(curr)
    for a in arr:
        if a != curr:
            answer.append(a)
            curr = a
    return answer