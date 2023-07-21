import sys
from itertools import combinations
input = sys.stdin.readline

def dist(r1, c1, r2, c2): # 거리 구하는 함수
    return abs(r1-r2) + abs(c1-c2)

N, M = map(int, input().split())

city = []
house = []
chicken = []

for _ in range(N):
    row = list(map(int, input().split()))
    city.append(row)

for r in range(N): # 집과 치킨집의 위치 저장
    for c in range(N):
        if city[r][c] == 1:
            house.append((r,c))
        elif city[r][c] == 2:
            chicken.append((r,c))

ans = 0

temp_ans = sys.maxsize  
for chick in combinations(chicken, M):
    temp = 0
    for r1, c1 in house:
        min_dist = sys.maxsize
        for r2, c2 in chick:
            cur_dist = dist(r1,c1,r2,c2)
            if cur_dist < min_dist:
                min_dist = cur_dist
        temp += min_dist
    if temp < temp_ans:
        temp_ans = temp
ans = temp_ans

print(ans)