import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
result = []
for i in range(n):
	result.append(s[i:])

result.sort()
for r in result:
	print(r)