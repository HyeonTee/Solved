from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	nums = list(map(int, input().split()))
	cnt = 0
	q = deque()
	for i, num in enumerate(nums):
		q.append((num, i))

	while q:
		if q[0][0] < max(q, key=lambda x: x[0])[0]:
			q.rotate(-1)
		else:
			cnt += 1
			if q[0][1] == m:
				print(cnt)
				break
			else:
				q.popleft()