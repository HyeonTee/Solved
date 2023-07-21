import sys
input = sys.stdin.readline

A, B, C = map(int,input().split())

ans_list = []
visited = [[[False] * (C+1) for _ in range(B+1)] for _ in range(A+1)]

def dfs(x, y, z):
    if x == 0:
        ans_list.append(z)
    visited[x][y][z] = True
    # A에서 B로
    pour = min(x, B-y) 
    if not visited[x-pour][y+pour][z]:
        dfs(x-pour, y+pour, z)
    # B에서 A로
    pour = min(A-x, y)
    if not visited[x+pour][y-pour][z]:
        dfs(x+pour, y-pour, z)
    # A에서 C로
    pour = min(x, C-z)
    if not visited[x-pour][y][z+pour]:
        dfs(x-pour, y, z+pour)
    # C에서 A로
    pour = min(A-x, z)
    if not visited[x+pour][y][z-pour]:
        dfs(x+pour, y, z-pour)
    # B에서 C로
    pour = min(y, C-z)
    if not visited[x][y-pour][z+pour]:
        dfs(x, y-pour, z+pour)
    # C에서 B로
    pour = min(B-y, z)
    if not visited[x][y+pour][z-pour]:
        dfs(x, y+pour, z-pour)

dfs(0, 0, C)

ans_list.sort()
print(*ans_list)