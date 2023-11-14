import sys
input = sys.stdin.readline

def is_valid(num):
	num_str = str(num)
	n = len(num_str)
	d = int(num_str[1]) - int(num_str[0])
	for i in range(n-1):
		dt = int(num_str[i+1]) - int(num_str[i])
		if d != dt:
			return False
	return True

n = int(input())

if n < 100:
	print(n)
else:
	cnt = 99
	for i in range(100, n+1):
		if is_valid(i):
			cnt += 1
	print(cnt)