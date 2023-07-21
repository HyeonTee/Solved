def solution(citations):
    # 인용된 수를 내림차순 정렬
    n = len(citations)
    citations.sort(reverse = True)
	# n부터 0까지 h를 줄여나가면서
    for h in range(n, -1, -1):
        cnt = 0
        # h번 이상 인용된 논문 count, 내림차순이니 인용이 h이하라면 바로 break
        for citation in citations:
            if citation >= h:
                cnt += 1
            else:
                break;
        # count 값이 처음으로 h 이상인 순간이 가장 큰 h이므로 바로 return        
        if cnt >= h:
            return h