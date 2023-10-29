from collections import deque

n, k = map(int, input().split())

nums = deque(list(range(1, n+1)))
ans = []
cnt = 1
while nums:
	tmp = nums.popleft()
	if cnt % k:
		nums.append(tmp)
	else:
		ans.append(tmp)
	cnt += 1

print("<", end = "")
for i in range(n-1):
	print(ans[i], end = ", ")
print(ans[-1], end = "")
print(">")