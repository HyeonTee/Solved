import sys
input = sys.stdin.readline

def solution(n, q):
	rev_base = []

	while n > 0:
		n, mod = divmod(n, q)
		rev_base.append(mod)

	return rev_base[::-1]

a, b = map(int, input().split())
n = int(input())
nums = list(map(int, input().split()))

ans = []
decimal = 0
for i in range(n):
	decimal += nums[i] * (a ** (n-i-1))

print(*solution(decimal, b))