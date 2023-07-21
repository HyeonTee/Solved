# 다음 순서의 단어로 변환하는 함수 
def next(cur):
    nextchar = {"A":"E", "E":"I", "I":"O", "O":"U"}
    if cur[-1] != "U":
        cur = cur[:-1] + nextchar[cur[-1]]
    # 단어의 마지막 글자가 U면 U 떼고 next
    else:
        cur = next(cur[:-1])
    return cur

def solution(word):
    answer = 0
    cur = ""
    # 현재 단어가 word랑 같아질때까지 반복
    while cur != word:
        # 현재 단어가 5글자 미만이면 A 하나 더 붙여줌
        if len(cur) < 5:
            cur += "A"
        # 5글자가 되면 next함수
        else:
            cur = next(cur)
        # 몇 번째 단어인지 카운트
        answer += 1
    
    return answer