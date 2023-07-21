import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
domados = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if domados[i][j][k] == 1:
                queue.append((i,j,k))

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if domados[nz][nx][ny] == 0:
                domados[nz][nx][ny] = domados[z][x][y] + 1
                queue.append((nz, nx, ny))

result = -2
nomato = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            result = max(result, domados[i][j][k])
            if domados[i][j][k] == 0:
                nomato = True

if nomato:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)