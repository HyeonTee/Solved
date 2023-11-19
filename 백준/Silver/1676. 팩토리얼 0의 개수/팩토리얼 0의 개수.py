import sys
from math import gcd, lcm
input = sys.stdin.readline

def count_zero(n):
	cnt = 0
	for i in range(1, n+1):
		if i % 5 == 0:
			while (i % 5 == 0):
				i //= 5
				cnt += 1
	return cnt

n = int(input())
print(count_zero(n))