import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

def find_idx(num):
	result = 0
	for i in range(1, n+1):
		result += min(num // i, n)
	
	return result

lt = 1
rt = k

while lt <= rt:
	mid = (lt + rt) // 2
	idx = find_idx(mid)
	if idx >= k:
		ans = mid
		rt = mid - 1
	else:
		lt = mid + 1

print(ans)