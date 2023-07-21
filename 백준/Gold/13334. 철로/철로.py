import sys
import heapq

n = int(sys.stdin.readline())

ho_list_raw = []

for _ in range(n):
    h, o = map(int, sys.stdin.readline().split())
    if h > o:
        h, o = o, h
    heapq.heappush(ho_list_raw, (h, o))

d = int(sys.stdin.readline())

ho_list = []
for h, o in ho_list_raw:
    if o - h <= d:
        ho_list.append((h, o))

ho_list.sort(key = lambda x: x[1])
heap = []

cnt = 0
max_cnt = 0

for home, office in ho_list:
    while heap and heap[0] < office - d:
        heapq.heappop(heap)
        cnt -= 1
    heapq.heappush(heap, home)
    cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)