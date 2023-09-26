import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())

parent = {}
edges = {}
mark = {}

for i in range(1,N+1):
    edges[i] = []
    mark[i] = None

for _ in range(N-1):
    v, w = map(int, input().split())
    edges[v].append(w)
    edges[w].append(v)

def DFS(v):
    mark[v] = "visited"
    for w in edges[v]:
        if mark[w] != "visited":
            parent[w] = v
            DFS(w)

DFS(1)

for i in range(2, N+1):
    print(parent[i])