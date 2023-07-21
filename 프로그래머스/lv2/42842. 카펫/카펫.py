# width * heigh = brown + yellow
# width*2 + heigh*2 - 4 = brown
# 이차방정식

def solution2(brown, yellow):
    width = (((brown+4)**2 - 16*(brown+yellow))**0.5 + (brown+4))//4
    heigh = (brown+yellow)//width
    
    return [width, heigh]

def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            if (i*2 + (yellow//i)*2) == brown-4:
                return [yellow//i+2, i+2]