import sys
input = sys.stdin.readline

n, x = map(int, input().split())
hits = list(map(int, input().split()))

window = sum(hits[:x])
window_max = window
cnt = 1
for i in range(x, n):
	window += hits[i]
	window -= hits[i-x]
	if window > window_max:
		window_max = window
		cnt = 1
	elif window == window_max:
		cnt += 1

if window_max:
	print(window_max)
	print(cnt)
else:
	print("SAD")