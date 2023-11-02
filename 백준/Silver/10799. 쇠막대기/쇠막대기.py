import sys
input = sys.stdin.readline

arrange = input().rstrip()
n = len(arrange)

cnt = 0
ans = 0
for i in range(n):
	if arrange[i] == "(":
		cnt += 1
	else: # )
		cnt -= 1		
		if arrange[i-1] == "(":
			ans += cnt
		else:
			ans += 1

print(ans)