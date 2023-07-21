import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())

states = []
for _ in range(n):
    states.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a,b):
    queue = deque()
    temp = []
    queue.append((a,b))
    temp.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(states[nx][ny]-states[x][y])<=r:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    return temp

ans = 0
while True:
    is_moved = False
    visited = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                united = bfs(i,j)
                if len(united) > 1:
                    is_moved = True
                    united_avg = sum(states[a][b] for a,b in united) // len(united)
                    for a,b in united:
                        states[a][b] = united_avg
    if not is_moved:
        break
    ans += 1

print(ans)