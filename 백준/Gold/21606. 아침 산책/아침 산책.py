import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input().strip())
A = list(input().strip())

indoor = []
edges = {}
mark = {}
cnt = 0

for idx, io in enumerate(A):
    if int(io) == 1:
        indoor.append(idx+1)

for i in range(1,N+1):
    edges[i] = []

for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

def dfs(v):
    global cnt
    mark[v] = "visited"
    for w in edges[v]:
        if mark[w] != "visited":
            dfs(w)
        else:
            if w in indoor:
                cnt += 1

for v in indoor:
    for i in range(1,N+1):
        mark[i] = None
    
    dfs(v)

print(cnt)