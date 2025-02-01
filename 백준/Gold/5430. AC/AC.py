from collections import deque
import sys
input = sys.stdin.readline
import ast


t = int(input())
for _ in range(t):
	functions = input()
	n = int(input())
	int_list = ast.literal_eval(input())
	int_deque = deque(int_list)
	is_left = True
	finished = True
	for func in functions:
		if func == 'R':
			is_left = not is_left
		if func == 'D':
			if len(int_deque) == 0:
				print("error")
				finished = False
				break
			if is_left:
				int_deque.popleft()
			else:
				int_deque.pop()
	if  finished and is_left:
		print(f"[{','.join(map(str, int_deque))}]")
	elif finished and not is_left:
		int_deque.reverse()
		print(f"[{','.join(map(str, int_deque))}]")