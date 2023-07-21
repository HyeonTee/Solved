import sys
input = sys.stdin.readline

n = int(input())

stairs = [0] * (n+1)
for i in range(1,n+1):
    stairs[i] = int(input())

dp = [[0]*3 for _ in range(n+1)] # dp[i][j]: j칸 연속으로 i 까지 온 경우

dp[1][1] = stairs[1]

for i in range(2, n+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stairs[i]
    dp[i][2] = dp[i-1][1] + stairs[i]

print(max(dp[n][1], dp[n][2]))