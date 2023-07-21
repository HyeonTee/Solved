import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

rooms = []
heap = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    rooms.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited[0][0] = True
heappush(heap, (0, 0, 0))

while heap:
    c, x, y = heappop(heap)
    if x == n-1 and y == n-1:
        print(c)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if rooms[nx][ny] == 0:
                heappush(heap, (c+1, nx, ny))
            else:
                heappush(heap, (c, nx, ny))