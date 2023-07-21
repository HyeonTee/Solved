import sys
input = sys.stdin.readline

N = int(input())

price_list = [0] + list(map(int, input().split()))

dp = [0] * 1001

for num, price in enumerate(price_list):
    for i in range(num, N+1):
        dp[i] = max(dp[i], dp[i-num] + price)

print(dp[N])