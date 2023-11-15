import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

dist = {}
edges = {}
for i in range(1, n+1):
	dist[i] = {}
	edges[i] = []

for _ in range(n-1):
	a, b, c = map(int, input().split())
	edges[a].append(b)
	edges[b].append(a)
	dist[a][b] = c
	dist[b][a] = c

visited = [False] * (n+1)
max_dist = 0

def dfs(u, curr):
	global max_dist
	visited[u] = True
	max_dist = max(max_dist, curr)
	for v in edges[u]:
		if not visited[v]:
			dfs(v, curr + dist[u][v])

dfs(1, 0)

print(max_dist)