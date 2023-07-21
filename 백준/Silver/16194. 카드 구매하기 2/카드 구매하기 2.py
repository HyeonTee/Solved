import sys
input = sys.stdin.readline

N = int(input())

price_list = [0] + list(map(int, input().split()))

dp = [10000] * 1001
dp[0] = 0

for num, price in enumerate(price_list):
    for i in range(num, N+1):
        dp[i] = min(dp[i], dp[i-num] + price)

print(dp[N])