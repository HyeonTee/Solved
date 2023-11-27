import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0
candidate = []
for _ in range(n):
	p, l = map(int, input().split())
	mileages = list(map(int, input().split()))
	if p < l:
		candidate.append(1)
	else:
		mileages.sort(reverse=True)
		candidate.append(mileages[l-1])

candidate.sort()
for c in candidate:
	if c <= m:
		m -= c
		ans += 1
	else:
		break

print(ans)