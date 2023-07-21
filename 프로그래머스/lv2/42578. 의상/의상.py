def solution(clothes):
    c_dict = {} 
    
    for _, kind in clothes:
        if kind not in c_dict:
            c_dict[kind] = 1
        else:
            c_dict[kind] += 1
    
    answer = 1
    # 옷 종류별로 옷 가짓수 + 1(안입기)을 계속 곱해줌
    for c in c_dict.values():
        answer *= (c+1)
    
    return answer - 1 # 전부 안입기인 경우 제외