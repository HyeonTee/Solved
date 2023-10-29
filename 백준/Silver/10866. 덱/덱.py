from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

Q = deque()
for _ in range(n):
	command = input().split()
	if command[0] == "push_front":
		Q.appendleft(command[1])
	elif command[0] == "push_back":
		Q.append(command[1])
	elif command[0] == "pop_front":
		if not Q:
			print(-1)
		else:
			print(Q.popleft())
	elif command[0] == "pop_back":
		if not Q:
			print(-1)
		else:
			print(Q.pop())
	elif command[0] == "size":
		print(len(Q))
	elif command[0] == "empty":
		if not Q:
			print(1)
		else:
			print(0)
	elif command[0] == "front":
		if not Q:
			print(-1)
		else:
			print(Q[0])
	elif command[0] == "back":
		if not Q:
			print(-1)
		else:
			print(Q[-1])