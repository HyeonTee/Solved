from itertools import permutations
import math

N = int(input()) # 도시의 개수

cost_list = [None] * N 

for i in range(N):
    cost_list[i] = list(map(int, input().split()))

route_list = list(permutations(list(range(1,N)),N-1))


cost_min = math.inf
for route in route_list:
    cost_sum = 0
    cost_sum += cost_list[0][route[0]] # 1에서 route[0]으로 가는 비용
    if cost_list[0][route[0]] == 0:
        cost_sum = math.inf
    for i in range(len(route)-1):
        cost_sum += cost_list[route[i]][route[i+1]]
        if cost_list[route[i]][route[i+1]] == 0:
            cost_sum = math.inf
    cost_sum += cost_list[route[-1]][0] # route[-1]에서 1로 가는 비용
    if cost_list[route[-1]][0] == 0:
        cost_sum = math.inf
    if cost_sum < cost_min:
        cost_min = cost_sum

print(cost_min)