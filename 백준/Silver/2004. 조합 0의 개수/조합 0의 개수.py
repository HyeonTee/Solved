import sys
input = sys.stdin.readline

def cnt_five(num):
	cnt = 0
	while num:
		num //= 5
		cnt += num
	return cnt

def cnt_two(num):
	cnt = 0
	while num:
		num //= 2
		cnt += num
	return cnt

n, m = map(int, input().split())

cnt_5 = cnt_five(n) - cnt_five(n-m) - cnt_five(m)
cnt_2 = cnt_two(n) - cnt_two(n-m) - cnt_two(m)

print(min(cnt_5, cnt_2))