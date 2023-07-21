import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    mass, value = map(int, input().split())
    jewels.append((mass, value))

jewels.sort()

knapsacks = []
for _ in range(K):
    knapsacks.append(int(input()))

knapsacks.sort()

heap = []

val_sum = 0
jewel_idx = 0
for capacity in knapsacks:
    while jewel_idx < N and jewels[jewel_idx][0] <= capacity:
        heappush(heap, -jewels[jewel_idx][1])
        jewel_idx += 1
    if heap:
        val_sum -= heappop(heap)

print(val_sum)