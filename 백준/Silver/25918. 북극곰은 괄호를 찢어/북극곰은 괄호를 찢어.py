N = int(input())
S = input()

cnt = 0
ans = 0
for s in S:
	if s == '(':
		cnt += 1
	else:
		cnt -= 1
	if abs(cnt) > ans:
		ans = abs(cnt)

if cnt == 0:
	print(ans)
else:
	print(-1)