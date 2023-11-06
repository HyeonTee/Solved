import sys
input = sys.stdin.readline

prefix = list(input().rstrip())

result = ""
stack = []
for p in prefix:
	if p == "*" or p == "/":
		while stack and (stack[-1] == "*" or stack[-1] == "/"):
			result += stack.pop()
		stack.append(p)
	elif p == "+" or p == "-":
		while stack and stack[-1] != "(":
			result += stack.pop()
		stack.append(p)
	elif p == "(":
		stack.append(p)
	elif p == ")":
		while stack and stack[-1] != "(":
			result += stack.pop()
		stack.pop()
	else:
		result += p

while stack:
	result += stack.pop()

print(result)