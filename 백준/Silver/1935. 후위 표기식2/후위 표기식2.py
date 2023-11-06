import sys
input = sys.stdin.readline

n = int(input())
cal = list(input().rstrip())

num = {}
for i in range(n):
	num[chr(65+i)] = int(input())

stack = []
for c in cal:
	if c == "+":
		result = stack.pop() + stack.pop()
		stack.append(result)
	elif c == "-":
		result = - stack.pop() + stack.pop()
		stack.append(result)
	elif c == "*":
		result = stack.pop() * stack.pop()
		stack.append(result)
	elif c == "/":
		result = 1 / stack.pop() * stack.pop()
		stack.append(result)
	else:
		stack.append(num[c])

print("%.2f" %stack[0])