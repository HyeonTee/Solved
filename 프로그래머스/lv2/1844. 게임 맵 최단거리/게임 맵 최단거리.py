from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, n, m, maps):
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                
    return maps[n-1][m-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    answer = bfs(0, 0, n, m, maps)
    if answer > 1:
        return answer
    else:
        return -1