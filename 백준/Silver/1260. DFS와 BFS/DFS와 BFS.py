import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

edges = {}
mark_dfs = {}
mark_bfs = {}
queue = []


for i in range(1,N+1):
    edges[i] = []
    mark_dfs[i] = None
    mark_bfs[i] = None

for _ in range(M):
    v, w = map(int, input().split())
    edges[v].append(w)
    edges[w].append(v)

for i in range(1,N+1):
    edges[i].sort()

def DFS(v):
    print(v, end = " ")
    mark_dfs[v] = "visited"
    for w in edges[v]:
        if mark_dfs[w] != "visited":
            DFS(w)

def BFS(v):
    print(v, end = " ")
    mark_bfs[v] = "visited"
    queue.append(v)
    while queue:
        for w in edges[queue.pop(0)]:
            if mark_bfs[w] != "visited":
                print(w, end = " ")
                mark_bfs[w] = "visited"
                queue.append(w)

DFS(V)
print()
BFS(V)