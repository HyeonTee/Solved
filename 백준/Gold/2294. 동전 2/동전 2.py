import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [0] * n
cnt = {}

for i in range(n):
    coins[i] = int(input().strip())

for i in range(k+1):
    cnt[i] = float('inf')
cnt[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        cnt[i] = min(cnt[i], cnt[i - coin] + 1)
     
if cnt[k] != float('inf'):
    print(cnt[k])
else:
    print(-1)