# 크기가 조금씩 다른 직사각형 종이들을 어떻게 정리하는가:
# 종이들을 전부 눕히거나 세워서 정리함! 이를 구현
def solution(sizes):
    width_list = []
    heigh_list = []
    
    # width_list, heigh_list를 따로 만들어줌
    for width, heigh in sizes:
        width_list.append(width)
        heigh_list.append(heigh)
    
    # width 중 max값과 heigh 중 max값을 구해서
    width_max = max(width_list)
    heigh_max = max(heigh_list)
    
    # 만약 width_max가 전체 길이 중 가장 큰 값이면
    if width_max > heigh_max:
        for i in range(len(sizes)):
            # 명함 하나의 width, heigh중 큰 값을 전부 width로 바꿔줌
            if width_list[i] < heigh_list[i]:
                width_list[i], heigh_list[i] = heigh_list[i], width_list[i]
        # 더 작은 값들로만 구성시킨 새 heigh_list의 max값을 구해줌
        heigh_max = max(heigh_list)
    # heigh_max가 전체 길이 중 최대라도 똑같이 해줌
    else:
        for i in range(len(sizes)):
            if width_list[i] > heigh_list[i]:
                width_list[i], heigh_list[i] = heigh_list[i], width_list[i]
        width_max = max(width_list)
        
    return width_max * heigh_max