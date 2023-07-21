import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tiny_stone = set()
dp_table = [[10001] * (int((2*N)**0.5)+2) for _ in range(N+1)] # dp_table[i][j]: i까지 j의 속도로 가는 비용

for _ in range(M):
    tiny_stone.add(int(input()))

dp_table[1][0] = 0

for i in range(2,N+1):
    if i in tiny_stone:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp_table[i][v] = min(dp_table[i-v][v-1], dp_table[i-v][v], dp_table[i-v][v+1]) + 1

ans = min(dp_table[N])

if ans == 10001:
    print(-1)
else:
    print(ans)