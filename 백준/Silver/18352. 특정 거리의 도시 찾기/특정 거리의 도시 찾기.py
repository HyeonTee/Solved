import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

edges = {}
visited = {}
queue = deque([])
distance = {}
dis_k = []

for i in range(1,N+1):
    edges[i] = []
    visited[i] = False
    distance[i] = 0

for _ in range(M):
    v, w = map(int, input().split())
    edges[v].append(w)

def bfs(x):
    queue.append(x)
    visited[x] = True
    while queue:
        v = queue.popleft()
        for w in edges[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
                distance[w] = distance[v] + 1
                if distance[w] == K:
                    heapq.heappush(dis_k, w)

bfs(X)

if not dis_k:
    print(-1)
while dis_k:
    print(heapq.heappop(dis_k))