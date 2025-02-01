from collections import deque
import sys
input = sys.stdin.readline

def dfs(curr, idx):
	global result
	if curr == n // 2:
		start = 0
		link = 0
		for i in range(n):
			for j in range(n):
				if visited[i] and visited[j]:
					start += s[i][j]
				elif not visited[i] and not visited[j]:
					link += s[i][j]
		result = min(result, abs(start - link))
	else:
		for i in range(idx, n):
			if not visited[i]:
				visited[i] = True
				dfs(curr+1, i+1)
				visited[i] = False


n = int(input())
visited = [False] * n
result = float('inf')
s = []
for _ in range(n):
	s.append(list(map(int, input().split())))

dfs(0,0)

print(result)