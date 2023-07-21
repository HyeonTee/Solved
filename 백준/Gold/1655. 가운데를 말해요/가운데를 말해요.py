import sys
import heapq

N = int(sys.stdin.readline())

heap_lt = []
heap_rt = []

for i in range(N):
    n = int(sys.stdin.readline())
    
    if len(heap_lt) == len(heap_rt):
        heapq.heappush(heap_lt, -n)
    else:
        heapq.heappush(heap_rt, n)
    
    if heap_rt and -heap_lt[0] > heap_rt[0]:
        rt_min = heapq.heappop(heap_rt)
        lt_max = -heapq.heappop(heap_lt)
        heapq.heappush(heap_lt, -rt_min)
        heapq.heappush(heap_rt, lt_max)
    
    print(-heap_lt[0])