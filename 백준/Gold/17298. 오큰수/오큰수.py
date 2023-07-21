N = int(input())

A_list = list(map(int, input().split()))

stack = []

ans = [-1] * N

for i in range(N):
	while stack and (A_list[stack[-1]] < A_list[i]):
	    ans[stack.pop()] = A_list[i]
	
	stack.append(i)

print(*ans)