import sys
input = sys.stdin.readline

dp = {}
for i in range(-50,51):
    dp[i] = {}
for i in range(-50,51):
    for j in range(-50,51):
        dp[i][j] = {}
for i in range(-50,51):
    for j in range(-50,51):
        for k in range(-50,51):
            dp[i][j][k] = 1

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i<j and j<k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

for i in range(21,51):
    for j in range(1,51):
        for k in range(1,51):
            dp[i][j][k] = dp[20][20][20]

for i in range(1,51):
    for j in range(21,51):
        for k in range(1,51):
            dp[i][j][k] = dp[20][20][20]

for i in range(1,51):
    for j in range(1,51):
        for k in range(21,51):
            dp[i][j][k] = dp[20][20][20]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    ans = dp[a][b][c]

    print("w(%d, %d, %d) = %d" %(a, b, c, ans))