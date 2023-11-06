import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

memo = {}
for n in n_list:
	if n in memo:
		memo[n] += 1
	else:
		memo[n] = 1

for m in m_list:
	if m in memo:
		print(memo[m], end = " ")
	else:
		print(0, end = " ")