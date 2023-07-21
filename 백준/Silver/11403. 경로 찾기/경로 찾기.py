import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

edges = {}
for i in range(n):
    edges[i] = []

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            edges[i].append(j)

matrix = [[0] * n for _ in range(n)]

def dfs(v):
    for w in edges[v]:
        if not visited[w]:
            visited[w] = True
            dfs(w)

for i in range(n):
    visited = [False] * n
    dfs(i)
    for j in range(n):
        if visited[j]:
            matrix[i][j] = 1

for i in range(n):
    print(*matrix[i])