from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    dist = [[0] * 102 for _ in range(102)]
    
    for lx, ly, rx, ry in rectangle:
        # 거리를 2배로 해놓고 answer을 2로 나눠줄거임(1칸 차이나는 경우때문)
        lx, ly, rx, ry = lx*2, ly*2, rx*2, ry*2
        # 직사각형 테두리와 내부를 1로 채움
        for i in range(lx, rx+1):
            for j in range(ly, ry+1):
                graph[i][j] = 1
        # 직사각형 내부를 visited로 만듦
        for i in range(lx+1, rx):
            for j in range(ly+1, ry):
                visited[i][j] = True
        
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((characterX*2, characterY*2))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    
    answer = dist[itemX*2][itemY*2]//2
    
    return answer