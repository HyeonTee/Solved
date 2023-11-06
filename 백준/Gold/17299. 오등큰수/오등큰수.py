import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

cnt = {}
for num in num_list:
	if num not in cnt:
		cnt[num] = 1
	else:
		cnt[num] += 1

stack = []
result = [-1] * n

for i in range(n):
	while stack and cnt[num_list[stack[-1]]] < cnt[num_list[i]]:
		result[stack.pop()] = num_list[i]
	stack.append(i)

print(*result)