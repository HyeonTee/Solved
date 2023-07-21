import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ans = 0
num_list = []
visit = [[0] * M for _ in range(N)]

for _ in range(N):
    row = list(map(int, input().split()))
    num_list.append(row)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

max_val = max(map(max, num_list))

def dfs(r, c, idx, total):
    global ans # 결과값

    if ans >= total + max_val * (3-idx):
        return
    
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r,c,idx+1,total + num_list[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr,nc,idx+1,total+num_list[nr][nc])
                visit[nr][nc] = 0

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r,c,0,num_list[r][c])
        visit[r][c] = 0

print(ans)