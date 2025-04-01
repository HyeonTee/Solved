import sys
input = sys.stdin.readline

result = [[0, 0] for _ in range(41)]
result[0][0] = 1
result[1][1] = 1
for i in range(2, 41):
	result[i][0] = result[i-1][0] + result[i-2][0]
	result[i][1] = result[i-1][1] + result[i-2][1]


t = int(input())
for _ in range(t):
	n = int(input())
	print(result[n][0], result[n][1])