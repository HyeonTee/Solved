import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

sum_data = sum(data)
lt = (sum_data + m - 1) // m
rt = sum_data

while lt <= rt:
	mid = (lt + rt) // 2
	if mid < max(data):
		lt = mid + 1
		continue

	cnt, temp = 1, 0
	for i in range(n):
		if temp + data[i] <= mid:
			temp += data[i]
		else:
			temp = data[i]
			cnt += 1
	
	if cnt <= m:
		rt = mid - 1
	else:
		lt = mid + 1

print(lt)