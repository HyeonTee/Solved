import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [-X, X])