n = int(input())

dp = [[0] * 91 for _ in range(2)] #dp[i][j]: i로 끝나는 이찬수의 갯수

dp[1][1] = 1
dp[0][2] = 1

for i in range(2,n+1):
    dp[0][i] = dp[0][i-1] + dp[1][i-1]
    dp[1][i] = dp[0][i-1]

print(dp[0][n]+dp[1][n])