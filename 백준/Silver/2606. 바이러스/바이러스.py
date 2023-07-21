import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
M = int(input())

edges = {}
mark = {}
cnt = -1

for i in range(1,N+1):
    edges[i] = []
    mark[i] = None

for _ in range(M):
    v, w = map(int, input().split())
    edges[v].append(w)
    edges[w].append(v)

def DFS(v):
    global cnt
    mark[v] = "visited"
    cnt += 1
    for w in edges[v]:
        if mark[w] != "visited":
            DFS(w)

DFS(1)

print(cnt)