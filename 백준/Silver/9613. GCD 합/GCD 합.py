import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
for _ in range(n):
	nums = list(map(int, input().split()))
	length = len(nums)
	ans = 0
	for i in range(1, length):
		for j in range(i+1, length):
			ans += gcd(nums[i], nums[j])
	print(ans)
