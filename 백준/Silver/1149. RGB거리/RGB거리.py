from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
rgb = []
for _ in range(n):
	rgb.append(list(map(int, input().split())))
	
dp = [[0, 0, 0] for _ in range(n)]

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, n):
	dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
	dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
	dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
	
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))