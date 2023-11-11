S = input()

ans = [0] * 26

for s in S:
	ans[ord(s)-97] += 1

print(*ans)