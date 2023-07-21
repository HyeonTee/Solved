import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
mark = 1

for _ in range(N):
    house = list(input().strip())
    graph.append(house)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    graph[a][b] = mark
    queue = deque([(a,b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == '1':
                graph[nx][ny] = mark
                queue.append((nx, ny))

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            bfs(i,j)
            mark += 1

ans = [0] * mark
for i in range(N):
    for j in range(N):
        if graph[i][j] != '0':
            ans[graph[i][j]] += 1

ans.sort()
print(len(ans) - 1)
for i in range(1, len(ans)):
    print(ans[i])