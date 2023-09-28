import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())

parent = {}
edges = {}
visited = {}

for i in range(1,n+1):
    edges[i] = []
    visited[i] = False

for _ in range(n-1):
    v, w = map(int, input().split())
    edges[v].append(w)
    edges[w].append(v)

def dfs(v):
    visited[v] = True
    for w in edges[v]:
        if not visited[w]:
            parent[w] = v
            dfs(w)

dfs(1)

for i in range(2, n+1):
    print(parent[i])